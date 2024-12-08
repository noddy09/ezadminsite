# tests/mysql_test_setup.py

from django.db import models
from django.db import connections
from django.core.management import call_command

# MySQL Test Model Setup
class MySQLProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class MySQLCustomer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

def setup_mysql_db():
    # Create the tables and insert some test data
    with connections['mysql_db'].cursor() as cursor:
        cursor.execute("CREATE TABLE mysql_product (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), price DECIMAL(10,2));")
        cursor.execute("CREATE TABLE mysql_customer (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), email VARCHAR(255));")

        cursor.execute("INSERT INTO mysql_product (name, price) VALUES ('Product 1', 19.99), ('Product 2', 29.99);")
        cursor.execute("INSERT INTO mysql_customer (name, email) VALUES ('Customer 1', 'customer1@example.com'), ('Customer 2', 'customer2@example.com');")
