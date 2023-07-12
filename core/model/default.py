__author__ = 'Nagesh Mhapadi'

from django.db import models


class AllNodes(models.Model):
    node_name = models.CharField(max_length=128, blank=True, null=True)
    node_ip = models.CharField(max_length=64)
    node_hypervisor = models.CharField(max_length=13)
    updated_at = models.IntegerField()
    status = models.CharField(max_length=6)
    region = models.CharField(max_length=64)
    base_key = models.TextField(blank=True, null=True)
    secure_config = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_nodes'


class AllVms(models.Model):
    node = models.CharField(max_length=10)
    vm_id = models.CharField(max_length=36)
    node_type = models.CharField(max_length=14)
    mac_address = models.CharField(max_length=64, blank=True, null=True)
    ip = models.CharField(max_length=36)
    private_ip = models.CharField(max_length=36, blank=True, null=True)
    port_details = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=7)
    is_idle = models.CharField(max_length=5)
    can_accept_gameplay = models.CharField(max_length=5)
    status = models.CharField(max_length=6)
    active_user = models.CharField(max_length=255, blank=True, null=True)
    state_triggered_at = models.IntegerField()
    vm_config_type = models.CharField(max_length=64, blank=True, null=True)
    vm_class = models.CharField(max_length=6)
    vm_config_details = models.TextField(blank=True, null=True)
    ping_log = models.TextField(blank=True, null=True)
    events_log = models.TextField(blank=True, null=True)
    last_pingged_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'all_vms'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GameNodeMapping(models.Model):
    game_id = models.CharField(max_length=64)
    store = models.CharField(max_length=16)
    node_id = models.CharField(max_length=32)
    can_play = models.CharField(max_length=5)
    iso_details = models.TextField(blank=True, null=True)
    updated_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_node_mapping'


class PartnerNodeMapping(models.Model):
    id = models.IntegerField()
    partner_id = models.CharField(max_length=36)
    node_id = models.CharField(max_length=36)
    type = models.CharField(max_length=14)
    is_active = models.CharField(max_length=5)
    updated_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'partner_node_mapping'


class UserGameSessions(models.Model):
    unique_session_key = models.CharField(max_length=256, blank=True, null=True)
    session_id = models.CharField(max_length=128, blank=True, null=True)
    ip_launched_from = models.CharField(max_length=64, blank=True, null=True)
    user_agent_launched_from = models.CharField(max_length=256, blank=True, null=True)
    launched_time = models.IntegerField()
    state = models.CharField(max_length=36, blank=True, null=True)
    state_details = models.JSONField(blank=True, null=True)
    launch_payload = models.TextField(blank=True, null=True)
    launch_client_key = models.CharField(max_length=256, blank=True, null=True)
    launch_server_key = models.CharField(max_length=256, blank=True, null=True)
    server_daemon_token = models.CharField(max_length=256, blank=True, null=True)
    user_id = models.CharField(max_length=255)
    game_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_game_sessions'


class UserVmMapping(models.Model):
    user_id = models.CharField(max_length=128)
    vm_id = models.IntegerField()
    is_active = models.CharField(max_length=5)
    updated_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_vm_mapping'
