__author__ = 'Nagesh Mhapadi'

from django.db import models


class ApiKey(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    public_key = models.CharField(unique=True, max_length=32)
    private_key = models.CharField(unique=True, max_length=32)
    expires_at = models.DateTimeField(blank=True, null=True)
    partner = models.ForeignKey('Partner', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_key'


class Partner(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    logo = models.TextField(blank=True, null=True)
    partner_type = models.CharField(max_length=13)
    registration_limit = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'partner'


class PartnerAccessMapping(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=64)
    partner = models.ForeignKey(Partner, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partner_access_mapping'


class PartnerFeedsMapping(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    feed_id = models.IntegerField()
    partner = models.ForeignKey(Partner, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partner_feeds_mapping'


class PartnerGamesMapping(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    game_id = models.BigIntegerField()
    partner = models.ForeignKey(Partner, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partner_games_mapping'


class PartnerNodeMapping(models.Model):
    partner = models.ForeignKey(Partner, models.DO_NOTHING)
    node_id = models.CharField(max_length=36)
    type = models.CharField(max_length=14)
    is_active = models.CharField(max_length=5)
    updated_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'partner_node_mapping'


class PartnerUsersMapping(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(max_length=36)
    partner = models.ForeignKey(Partner, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partner_users_mapping'
