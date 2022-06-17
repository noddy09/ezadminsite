import re
import os
from django.core.management.base import BaseCommand, CommandError
from django.db import DEFAULT_DB_ALIAS, connections
from django.core.management import call_command
from django.core.management.commands.inspectdb import Command as DbInspect

class Command(DbInspect):
    """
    """
    help = "Creates admin site in 2 minute. # Maggie's competetor."

    def handle_lines(self):
        connection = connections['default']

        def table2model(table_name):
            return re.sub(r'[^a-zA-Z0-9]', '', table_name.title())

        with connection.cursor() as cursor:
            yield "__author__ = 'Nagesh Mhapadi'"
            yield ''
            yield 'from %s import models' % self.db_module
            known_models = []
            table_info = connection.introspection.get_table_list(cursor)

            # Determine types of tables and/or views to be introspected.
            types = {'t'}
            for table_name in sorted(info.name for info in table_info):
                try:
                    try:
                        relations = connection.introspection.get_relations(cursor, table_name)
                    except NotImplementedError:
                        relations = {}
                    try:
                        constraints = connection.introspection.get_constraints(cursor, table_name)
                    except NotImplementedError:
                        constraints = {}
                    primary_key_column = connection.introspection.get_primary_key_column(cursor, table_name)
                    unique_columns = [
                        c['columns'][0] for c in constraints.values()
                        if c['unique'] and len(c['columns']) == 1
                    ]
                    table_description = connection.introspection.get_table_description(cursor, table_name)
                except Exception as e:
                    yield "# Unable to inspect table '%s'" % table_name
                    yield "# The error was: %s" % e
                    continue

                yield ''
                yield ''
                yield 'class %s(models.Model):' % table2model(table_name)
                known_models.append(table2model(table_name))
                used_column_names = []  # Holds column names used in the table so far
                column_to_field_name = {}  # Maps column names to names of model fields
                for row in table_description:
                    comment_notes = []  # Holds Field notes, to be displayed in a Python comment.
                    extra_params = {}  # Holds Field parameters such as 'db_column'.
                    column_name = row.name
                    is_relation = column_name in relations

                    att_name, params, notes = self.normalize_col_name(
                        column_name, used_column_names, is_relation)
                    extra_params.update(params)
                    comment_notes.extend(notes)

                    used_column_names.append(att_name)
                    column_to_field_name[column_name] = att_name

                    # Add primary_key and unique, if necessary.
                    if column_name == primary_key_column:
                        extra_params['primary_key'] = True
                    elif column_name in unique_columns:
                        extra_params['unique'] = True

                    if is_relation:
                        if extra_params.pop('unique', False) or extra_params.get('primary_key'):
                            rel_type = 'OneToOneField'
                        else:
                            rel_type = 'ForeignKey'
                        rel_to = (
                            "self" if relations[column_name][1] == table_name
                            else table2model(relations[column_name][1])
                        )
                        if rel_to in known_models:
                            field_type = '%s(%s' % (rel_type, rel_to)
                        else:
                            field_type = "%s('%s'" % (rel_type, rel_to)
                    else:
                        # Calling `get_field_type` to get the field type string and any
                        # additional parameters and notes.
                        field_type, field_params, field_notes = self.get_field_type(connection, table_name, row)
                        extra_params.update(field_params)
                        comment_notes.extend(field_notes)

                        field_type += '('

                    # Don't output 'id = meta.AutoField(primary_key=True)', because
                    # that's assumed if it doesn't exist.
                    if att_name == 'id' and extra_params == {'primary_key': True}:
                        if field_type == 'AutoField(':
                            continue
                        elif field_type == connection.features.introspected_field_types['AutoField'] + '(':
                            comment_notes.append('AutoField?')

                    # Add 'null' and 'blank', if the 'null_ok' flag was present in the
                    # table description.
                    if row.null_ok:  # If it's NULL...
                        extra_params['blank'] = True
                        extra_params['null'] = True

                    field_desc = '%s = %s%s' % (
                        att_name,
                        # Custom fields will have a dotted path
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
                yield from self.get_meta(table_name, constraints, column_to_field_name, False, False)


    def handle(self, **options):
        print("I gurantee you, It will be done before your maggie gets ready.")

        # creating model from existing database
        try:
            with open("core/models.py", "w", encoding="utf-8") as output_file:
                for line in self.handle_lines():
                    output_file.write(line + '\n')
        except NotImplementedError:
            raise CommandError("Database inspection isn't supported for the currently selected database backend.")

        # registering models to admin site
        try:
            with open("core/admin.py", "w", encoding="utf-8") as output_file:
                output_file.write("""
from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass""")
        except Exception:
            raise CommandError("Unable to register models in admin site.")

        # make admin site ready with required models.
        try:
            call_command('makemigrations')
            call_command('migrate')
        except Exception:
            raise CommandError("Unable to migrate basic auth and site related tables.")

        try:
            from django.contrib.auth.models import User

            u = User(username='admin')
            u.set_password('Pass@123')
            u.is_superuser = True
            u.is_staff = True
            u.save()
        except Exception:
            raise CommandError("Unable to create superuser for site. User command 'createsuperuser' and logged in with same.")
        
        print("Superuser has been created with default login ID 'admin'. You can create your on by using 'createsuperuser' command.")