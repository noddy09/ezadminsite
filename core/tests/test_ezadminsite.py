# tests/test_ezadminsite.py

import unittest
from django.core.management import call_command
from django.test import TestCase
from django.db import connections
from django.apps import apps
import os

class EzAdminSiteTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up PostgreSQL and MySQL data
        from tests.postgresql_test_setup import setup_postgres_db
        from tests.mysql_test_setup import setup_mysql_db

        # Set up PostgreSQL test data
        setup_postgres_db()

        # Set up MySQL test data
        setup_mysql_db()

    def test_generate_postgres_models_and_admin(self):
        # Run the build_admin_panel command for PostgreSQL
        call_command('build_admin_panel')

        # Check if the model files for PostgreSQL were created
        postgres_model_file = os.path.join('core', 'models', 'postgres.py')
        self.assertTrue(os.path.exists(postgres_model_file))

        # Check if the admin file for PostgreSQL was created
        postgres_admin_file = os.path.join('core', 'admin', 'postgres.py')
        self.assertTrue(os.path.exists(postgres_admin_file))

        # Verify that the PostgreSQL models were registered
        app_models = apps.get_models()
        model_names = [model.__name__ for model in app_models]
        self.assertIn('PostgresProduct', model_names)
        self.assertIn('PostgresCustomer', model_names)

    def test_generate_mysql_models_and_admin(self):
        # Run the build_admin_panel command for MySQL
        call_command('build_admin_panel')

        # Check if the model files for MySQL were created
        mysql_model_file = os.path.join('core', 'models', 'mysql_db.py')
        self.assertTrue(os.path.exists(mysql_model_file))

        # Check if the admin file for MySQL was created
        mysql_admin_file = os.path.join('core', 'admin', 'mysql_db.py')
        self.assertTrue(os.path.exists(mysql_admin_file))

        # Verify that the MySQL models were registered
        app_models = apps.get_models()
        model_names = [model.__name__ for model in app_models]
        self.assertIn('MySQLProduct', model_names)
        self.assertIn('MySQLCustomer', model_names)

    def test_postgres_data_integrity(self):
        # Verify that the sample data for PostgreSQL is available
        from core.models.postgres import PostgresProduct, PostgresCustomer

        product = PostgresProduct.objects.first()
        customer = PostgresCustomer.objects.first()

        self.assertEqual(product.name, 'Product 1')
        self.assertEqual(customer.name, 'Customer 1')

    def test_mysql_data_integrity(self):
        # Verify that the sample data for MySQL is available
        from core.models.mysql_db import MySQLProduct, MySQLCustomer

        product = MySQLProduct.objects.first()
        customer = MySQLCustomer.objects.first()

        self.assertEqual(product.name, 'Product 1')
        self.assertEqual(customer.name, 'Customer 1')
