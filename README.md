# EzAdminSite 
Django based web application which can easily create django admin site based on existing/ legacy database in just one command.


**Objective:**

The objective of the EzAdminSite library is to automate the creation of Django admin site models and admin files based on the existing tables in the
database.

**Features:**

- Iterates through database `DATABASES` config values from settings.py.
- Creates models for each table found in the database.
- Creates admin.py files for each model, allowing for admin site registration.

**Command:**

The provided code snippet includes a Django command called `build_admin_panel` that performs the following steps:

1. Creates models.py and admin.py files.
2. Registers models in the admin site.
3. Migrates basic auth and site-related tables.
4. Creates a superuser with default login credentials.

**Implementation:**

- The command iterates through the database tables using introspection.
- For each table, it generates a corresponding model class with fields based on the table columns.
- It also creates an admin registration entry in admin.py.
- The command handles exceptions and provides informative error messages.

**Usage:**

To use the library, simply run the `build_admin_panel` command in the terminal.

**Example:**

```
python manage.py build_admin_panel
```

**Benefits:**

- Automates the admin site creation process.
- Saves time and effort in manually creating models and admin files.
- Ensures consistency and accuracy in admin site registration.

**Note:**

- The command requires the necessary database credentials to be set in the settings.py file.
- It is recommended to review and adjust the generated models and admin files before deploying to production.
