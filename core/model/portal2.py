__author__ = 'Nagesh Mhapadi'

from django.db import models


class FailedJobs(models.Model):
    id = models.PositiveBigIntegerField()
    uuid = models.CharField(max_length=255)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Modules(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255)
    is_visible_to_admin = models.CharField(max_length=3)
    is_visible_to_partner = models.CharField(max_length=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'modules'


class OtpValidations(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=255)
    otp = models.CharField(max_length=255)
    status = models.CharField(max_length=255, db_comment='1 = Active, 2 = Inactive')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'otp_validations'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class Permissions(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    module_id = models.CharField(max_length=36)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'permissions'


class RoleModulePermission(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    role_id = models.CharField(max_length=36)
    module_permission = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'role_module_permission'


class Roles(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255)
    role_type = models.CharField(max_length=7)
    partner_id = models.CharField(max_length=36, blank=True, null=True)
    status = models.CharField(max_length=8)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'roles'


class UserActivityLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    module_id = models.IntegerField(blank=True, null=True)
    module_name = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_activity_logs'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    role_id = models.CharField(max_length=36)
    user_type = models.CharField(max_length=7)
    status = models.CharField(max_length=8, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
