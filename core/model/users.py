__author__ = 'Nagesh Mhapadi'

from django.db import models


class Payment(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    status = models.CharField(max_length=10)
    user_ip = models.CharField(max_length=64)
    user_device = models.CharField(max_length=6)
    device_agent = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING)
    subscription_package = models.ForeignKey('SubscriptionPackages', models.DO_NOTHING)
    provider = models.CharField(max_length=16, blank=True, null=True)
    provider_payment_id = models.CharField(max_length=256, blank=True, null=True)
    payment_method = models.CharField(max_length=16, blank=True, null=True)
    logs = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'


class SubscriptionPackages(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    created_at = models.IntegerField()
    updated_at = models.IntegerField()
    is_free = models.CharField(max_length=5)
    value = models.FloatField()
    currency = models.CharField(max_length=3)
    is_active = models.CharField(max_length=5)
    plan_name = models.CharField(max_length=256)
    plan_description = models.TextField(blank=True, null=True)
    can_run_4k = models.CharField(max_length=5)
    can_run_mobile = models.CharField(max_length=5)
    can_run_hd = models.CharField(max_length=5)
    deleted_at = models.DateTimeField(blank=True, null=True)
    plan_duration_in_days = models.IntegerField()
    total_offered_tokens = models.FloatField()
    package_type = models.CharField(max_length=5)
    target_region = models.CharField(max_length=128, blank=True, null=True)
    partner_id = models.CharField(max_length=128, blank=True, null=True)
    plan_config = models.JSONField(blank=True, null=True)
    is_live_for_purchase = models.CharField(max_length=5)
    visibility_type = models.TextField()

    class Meta:
        managed = False
        db_table = 'subscription_packages'


class Subscriptions(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    amount = models.DecimalField(max_digits=10, decimal_places=5)
    brought_price = models.DecimalField(max_digits=10, decimal_places=5)
    was_free_plan = models.CharField(max_length=5)
    offer_id = models.CharField(max_length=12, blank=True, null=True)
    source_partner_id = models.CharField(max_length=128, blank=True, null=True)
    subscription_brought_at_time = models.DateTimeField()
    subscription_active_from = models.DateTimeField()
    subscription_active_till = models.DateTimeField()
    subscription_status = models.CharField(max_length=7)
    subscription_package = models.ForeignKey(SubscriptionPackages, models.DO_NOTHING)
    payment = models.OneToOneField(Payment, models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    deleted_at = models.DateTimeField(blank=True, null=True)
    remaining_tokens = models.FloatField()

    class Meta:
        managed = False
        db_table = 'subscriptions'


class UserStreamSessions(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    game_id = models.CharField(max_length=128)
    node_id = models.CharField(max_length=128)
    vm_id = models.CharField(max_length=128)
    token_per_minute = models.FloatField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    total_tokens_used = models.FloatField()
    ip = models.CharField(max_length=64)
    user_agent = models.CharField(max_length=255)
    device = models.CharField(max_length=6, blank=True, null=True)
    session_id = models.CharField(max_length=256)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_stream_sessions'


class Users(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    username = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=7)
    email = models.CharField(unique=True, max_length=255)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.TextField(blank=True, null=True)
    background_image = models.TextField(blank=True, null=True)
    is_verified_profile = models.CharField(max_length=5)
    number_of_followers = models.IntegerField()
    number_of_following = models.IntegerField()
    social_media_details = models.TextField(blank=True, null=True)
    password_hash = models.CharField(max_length=512)
    password_reset_token = models.CharField(max_length=1024, blank=True, null=True)
    last_password_reset = models.DateTimeField()
    number_of_password_resets = models.IntegerField()
    registration_token = models.CharField(max_length=1024, blank=True, null=True)
    status = models.CharField(max_length=10)
    user_type = models.CharField(max_length=8)
    signedup_timestamp = models.DateTimeField()
    is_automatic_subscription_renewable = models.CharField(max_length=5)
    signedup_ip = models.CharField(max_length=128)
    signup_uagent = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField()
    last_login_timestamp = models.DateTimeField()
    referred_by_id = models.CharField(max_length=36, blank=True, null=True)
    number_of_otp_sent = models.IntegerField()
    phone = models.CharField(unique=True, max_length=20)
    deleted_at = models.DateTimeField(blank=True, null=True)
    config = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Wishlist(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    game_id = models.CharField(max_length=255)
    user = models.ForeignKey(Users, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wishlist'
