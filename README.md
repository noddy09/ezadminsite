# EzAdminSite

EzAdminSite is a Django-based library that automates the creation of a Django admin site for an existing or legacy database with just one command. It generates models and admin registrations dynamically, allowing you to manage your legacy databases via the Django admin interface seamlessly.

## **Objective**

The objective of EzAdminSite is to automate the creation of Django admin site models and admin files based on existing database tables. It eliminates the need for manually creating model classes and admin registrations, saving time and reducing errors.

## **Features**

- Iterates through all database configurations (`DATABASES`) defined in `settings.py`.
- Creates model classes for each table found in the database.
- Dynamically generates `admin.py` files for each model, allowing them to be registered in the Django admin site.
- Supports multiple databases by generating models and admin files for each database alias.
- Handles the creation of `models/__init__.py` and `admin/__init__.py` to dynamically import all model and admin files for each database.
- Ensures proper field handling, including unique constraints and foreign key relationships.

## **Command**

The library provides a Django command called `build_admin_panel` that automates the following tasks:

1. Creates `models.py` files for each database with model classes corresponding to existing database tables.
2. Creates dynamic `admin.py` files that register models for the Django admin site.
3. Registers models automatically to the admin site for easy management.
4. Runs migrations to ensure any necessary database changes (like auth and site-related tables) are applied.
5. Creates a superuser with default login credentials (`admin` with password `Pass@123`) for immediate access to the admin interface.

## **Usage**

1. Install the library and add it to your `INSTALLED_APPS` in `settings.py`.

2. Add the following to your `settings.py`:
    ```python
    DATABASE_ROUTERS = ['core.models.DynamicDatabaseRouter']
    ```

3. Run the command to generate the admin site:
    ```bash
    python manage.py build_admin_panel
    ```

4. Access the Django admin site at `/admin` using the default superuser credentials:
    - Username: `admin`
    - Password: `Pass@123`

   Alternatively, you can create your own superuser by running `python manage.py createsuperuser`.

## **Implementation**

- **Dynamic Model Generation**: The command introspects the database, finding all tables across multiple databases. For each table, it generates a model with fields corresponding to the columns in the table.
  
- **Dynamic Admin Registration**: For each model generated, an `admin.py` file is created, and the models are registered with the Django admin site. This allows for immediate use of the admin interface.

- **Database Router**: A custom `DynamicDatabaseRouter` is used to manage database routing for each model, ensuring models are correctly directed to their respective databases.

- **Exception Handling**: The command is designed to handle various exceptions, providing clear error messages for missing configurations or database issues.

## **Folder Structure**

After running the command, the following folder structure is created:

```
core/
 ├── admin/
 │ ├── init.py # Imports for all admin registration files
 │ ├── {db_alias}.py # Admin file for each database alias
 ├── models/ │ ├── init.py # Imports for all model files
 │ ├── {db_alias}.py # Model file for each database alias
```

Each model file corresponds to a database alias and contains a `models.py` file with generated model classes based on the respective database tables. Similarly, the `admin.py` files automatically register models for each database.

## **Example**

### Before running the command:
You have an existing database with tables `user`, `order`, and `product`.

### After running the command:
- For each database in your `DATABASES` configuration, EzAdminSite will:
    1. Generate model classes for each table (e.g., `User`, `Order`, `Product`).
    2. Create corresponding `admin.py` files to register these models in the admin site.
    3. Dynamically update `models/__init__.py` and `admin/__init__.py` with imports for the newly created files.
    4. Run migrations and create a superuser.

### Example Command Output:
```bash
python manage.py build_admin_panel
```

## **Benefits**

- **Automates admin site creation**: EzAdminSite eliminates the tedious task of manually creating models and registering them in the admin interface.
- **Handles multiple databases**: Supports generating models and admin registrations for all databases listed in `DATABASES`.
- **Consistency and accuracy**: Ensures that the generated models and admin files are consistent with the database schema, including handling constraints like unique fields and foreign keys.
- **Easy to use**: With just a single command, your Django admin site is ready to manage existing database tables.

## **Note**

- The command requires the necessary database credentials to be set in the `settings.py` file.
- It is recommended to review the generated models and admin files before deploying them to production, as additional customization may be required.
- The generated superuser can be used immediately to access the admin site, but it's also possible to create additional superusers using the `createsuperuser` command.

