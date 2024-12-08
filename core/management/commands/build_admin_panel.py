import re
import os
from django.core.management.base import BaseCommand, CommandError
from django.db import connections
from django.core.management import call_command
from django.contrib.admin.sites import AlreadyRegistered

class Command(BaseCommand):
    help = "Creates admin site in 2 minutes. # Maggie's competitor."

    def handle_lines(self, db_alias):
        """
        Generate model definitions for the specified database alias.
        """
        connection = connections[db_alias]

        def table2model(table_name):
            return re.sub(r'[^a-zA-Z0-9]', '', table_name.title())

        with connection.cursor() as cursor:
            yield "__author__ = 'Nagesh Mhapadi'"
            yield ''
            yield 'from django.db import models'
            known_models = []
            table_info = connection.introspection.get_table_list(cursor)

            for table_name in sorted(info.name for info in table_info):
                try:
                    relations = connection.introspection.get_relations(cursor, table_name)
                    constraints = connection.introspection.get_constraints(cursor, table_name)
                    primary_key_column = connection.introspection.get_primary_key_column(cursor, table_name)
                    table_description = connection.introspection.get_table_description(cursor, table_name)
                except Exception as e:
                    yield "# Unable to inspect table '%s'" % table_name
                    yield "# The error was: %s" % e
                    continue

                yield ''
                yield 'class %s(models.Model):' % table2model(table_name)

                # Specify the app label to associate the model with the correct database in the router
                yield '    class Meta:'
                yield f'        app_label = "{db_alias}"'  # Associate with the database alias

                known_models.append(table2model(table_name))
                used_column_names = []  # Holds column names used in the table
                column_to_field_name = {}  # Maps column names to names of model fields

                for row in table_description:
                    comment_notes = []  # Holds Field notes
                    extra_params = {}  # Holds extra field parameters
                    column_name = row.name
                    is_relation = column_name in relations

                    att_name, params, notes = self.normalize_col_name(
                        column_name, used_column_names, is_relation)
                    extra_params.update(params)
                    comment_notes.extend(notes)

                    used_column_names.append(att_name)
                    column_to_field_name[column_name] = att_name

                    # Add primary_key and unique, if necessary
                    if column_name == primary_key_column:
                        extra_params['primary_key'] = True
                    elif column_name in constraints and constraints[column_name]['unique']:
                        extra_params['unique'] = True  # Ensure unique is set

                    if is_relation:
                        if extra_params.pop('unique', False) or extra_params.get('primary_key'):
                            rel_type = 'OneToOneField'
                        else:
                            rel_type = 'ForeignKey'
                        rel_to = (
                            "self" if relations[column_name][1] == table_name
                            else table2model(relations[column_name][1])
                        )
                        field_type = '%s(%s' % (rel_type, rel_to)
                    else:
                        field_type, field_params, field_notes = self.get_field_type(connection, table_name, row)
                        extra_params.update(field_params)
                        comment_notes.extend(field_notes)
                        field_type += '('

                    # Exclude unnecessary `AutoField` for 'id' column
                    if att_name == 'id' and extra_params == {'primary_key': True}:
                        continue

                    # Add 'null' and 'blank' flags if the column allows NULL
                    if row.null_ok:
                        extra_params['blank'] = True
                        extra_params['null'] = True

                    # Assemble the field description
                    field_desc = '%s = %s%s' % (
                        att_name,
                        '' if '.' in field_type else 'models.',
                        field_type,
                    )

                    if field_type.startswith(('ForeignKey(', 'OneToOneField(')):
                        field_desc += ', models.DO_NOTHING'

                    if extra_params:
                        if not field_desc.endswith('('):
                            field_desc += ', '
                        field_desc += ', '.join('%s=%r' % (k, v) for k, v in extra_params.items())
                    field_desc += ')'
                    if comment_notes:
                        field_desc += '  # ' + ' '.join(comment_notes)

                    yield '    %s' % field_desc

                # Add model meta information (e.g., constraints)
                yield from self.get_meta(table_name, constraints, column_to_field_name, False, False)

    def handle(self, **options):
        """
        Handle the command execution.
        """
        print("Starting the process of building the admin panel...")

        # Create models directory if it doesn't exist
        if not os.path.exists('models'):
            os.makedirs('models')

        # Track which models we created for the current database alias
        created_model_files = []

        # Generate models for each database alias
        for db_alias in connections:
            try:
                model_filename = os.path.join('models', f"{db_alias}.py")
                with open(model_filename, "w", encoding="utf-8") as output_file:
                    for line in self.handle_lines(db_alias):
                        output_file.write(line + '\n')
                
                # Track the model file we just created
                created_model_files.append(f"{db_alias}.py")

            except Exception as e:
                raise CommandError(f"Error generating models for database '{db_alias}': {str(e)}")

        # Now, update models/__init__.py to import the newly created models
        try:
            with open('models/__init__.py', 'a', encoding='utf-8') as init_file:
                for model_filename in created_model_files:
                    init_file.write(f'from core.models.{model_filename[:-3]} import *\n')
        except Exception as e:
            raise CommandError(f"Error updating models/__init__.py: {str(e)}")

        # Admin registration for each database alias
        try:
            # Ensure admin directory exists
            if not os.path.exists('admin'):
                os.makedirs('admin')

            admin_init_file = os.path.join('admin', f'{db_alias}.py')

            with open(admin_init_file, "w", encoding="utf-8") as output_file:
                output_file.write("""
from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

# Register all models in the admin site
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
""")

            # Update admin/__init__.py to import the new admin files
            with open('admin/__init__.py', 'a', encoding='utf-8') as admin_init_file:
                for model_filename in created_model_files:
                    admin_init_file.write(f'from core.admin.{model_filename[:-3]} import *\n')

        except Exception as e:
            raise CommandError(f"Error generating admin registrations: {str(e)}")

        # Run migrations to set up database tables
        try:
            call_command('makemigrations')
            call_command('migrate')
        except Exception as e:
            raise CommandError(f"Error during migration: {str(e)}")

        # Create a superuser if not already created
        try:
            from django.contrib.auth.models import User
            if not User.objects.filter(username='admin').exists():
                user = User(username='admin')
                user.set_password('Pass@123')
                user.is_superuser = True
                user.is_staff = True
                user.save()
        except Exception as e:
            raise CommandError(f"Error creating superuser: {str(e)}")

        print("Superuser has been created with default login ID 'admin'. You can create your own using 'createsuperuser' command.")
