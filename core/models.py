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
        
__author__ = 'Nagesh Mhapadi'

from django.db import models


class Alias(models.Model):
    id = models.BigAutoField(primary_key=True)
    game_id = models.BigIntegerField()
    name = models.CharField(max_length=500)
    src = models.CharField(max_length=6)
    created_at = models.IntegerField()
    updated_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alias'


class ConfigTemp(models.Model):
    oplay_id = models.CharField(max_length=128)
    number_1games_launch_config = models.TextField(db_column='1games_launch_config', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'config_temp'


class Deals(models.Model):
    id = models.BigAutoField(primary_key=True)
    game_id = models.BigIntegerField(blank=True, null=True)
    deal_id = models.CharField(max_length=255, blank=True, null=True)
    sale_price = models.CharField(max_length=255, blank=True, null=True)
    normal_price = models.CharField(max_length=255, blank=True, null=True)
    savings = models.CharField(max_length=255, blank=True, null=True)
    is_on_sale = models.CharField(max_length=5)
    store_id = models.IntegerField()
    store_link = models.CharField(max_length=250, blank=True, null=True)
    deal_rating = models.FloatField(blank=True, null=True)
    deal_source = models.CharField(max_length=10)
    created_at = models.IntegerField()
    updated_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'deals'


class DeveloperPublisherMapping(models.Model):
    id = models.BigAutoField(primary_key=True)
    developer_publisher = models.ForeignKey('DeveloperPublishers', models.DO_NOTHING)
    game = models.ForeignKey('Games', models.DO_NOTHING)
    updated_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'developer_publisher_mapping'


class DeveloperPublishers(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=9)
    rawg_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=1024, blank=True, null=True)
    games_count = models.IntegerField(blank=True, null=True)
    oplay_games_count = models.IntegerField(blank=True, null=True)
    created_at = models.IntegerField()
    updated_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'developer_publishers'


class Feeds(models.Model):
    feed_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    content_payload = models.TextField(blank=True, null=True)
    date_added = models.IntegerField()
    date_updated = models.IntegerField()
    status = models.CharField(max_length=6)
    index_number = models.IntegerField()
    is_test = models.CharField(max_length=5)
    is_personalized = models.CharField(max_length=5)
    target_payload = models.TextField(blank=True, null=True)
    min_content = models.IntegerField()
    max_content = models.IntegerField()
    creator_user_id = models.CharField(max_length=36)
    feed_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'feeds'


class GameSeries(models.Model):
    game_id1 = models.BigIntegerField()
    game_id2 = models.BigIntegerField()
    updated_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'game_series'


class Games(models.Model):
    id = models.BigAutoField(primary_key=True)
    oplay_id = models.CharField(max_length=128)
    title = models.CharField(max_length=1024, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    release_date = models.CharField(max_length=16)
    poster_image = models.CharField(max_length=1024, blank=True, null=True)
    igdb_id = models.IntegerField(blank=True, null=True)
    steam_id = models.IntegerField(blank=True, null=True)
    is_downloaded = models.CharField(max_length=5)
    background_image = models.CharField(max_length=1024, blank=True, null=True)
    text_background_image = models.CharField(max_length=1024, blank=True, null=True)
    oneplay_popularity_score = models.FloatField()
    metacritic_url = models.CharField(max_length=255, blank=True, null=True)
    metacritic_score = models.IntegerField(blank=True, null=True)
    reddit_url = models.CharField(max_length=255, blank=True, null=True)
    official_website = models.CharField(max_length=1024, blank=True, null=True)
    age_rating = models.CharField(max_length=32, blank=True, null=True)
    rawg_id = models.CharField(max_length=10)
    cheapshark_id = models.CharField(max_length=10, blank=True, null=True)
    is_released = models.CharField(max_length=5)
    status = models.CharField(max_length=6)
    is_categorized = models.CharField(max_length=5)
    is_indexed = models.IntegerField(blank=True, null=True)
    created_at = models.IntegerField()
    updated_at = models.IntegerField()
    is_oneplay_supported = models.CharField(max_length=5, blank=True, null=True)
    text_logo = models.CharField(max_length=255, blank=True, null=True)
    games_launch_config = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    is_parent_game = models.CharField(max_length=5)
    parent_game_id = models.BigIntegerField(blank=True, null=True)
    is_edited = models.CharField(max_length=5)
    is_free = models.CharField(max_length=5)
    mashhead_video = models.CharField(max_length=1024, blank=True, null=True)
    trailer_video = models.CharField(max_length=1024, blank=True, null=True)
    boxplay_video = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'games'


class GenreMapping(models.Model):
    id = models.BigAutoField(primary_key=True)
    genre = models.ForeignKey('Genres', models.DO_NOTHING)
    game = models.ForeignKey(Games, models.DO_NOTHING)
    updated_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'genre_mapping'


class Genres(models.Model):
    id = models.BigAutoField(primary_key=True)
    rawg_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=1024, blank=True, null=True)
    games_count = models.IntegerField(blank=True, null=True)
    oplay_games_count = models.IntegerField(blank=True, null=True)
    created_at = models.IntegerField()
    updated_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'genres'


class Media(models.Model):
    id = models.BigAutoField(primary_key=True)
    rawg_id = models.IntegerField(blank=True, null=True)
    media_type = models.CharField(max_length=5)
    link = models.CharField(max_length=255, blank=True, null=True)
    is_downloaded = models.CharField(max_length=5)
    source = models.CharField(max_length=7)
    game = models.ForeignKey(Games, models.DO_NOTHING)
    created_at = models.IntegerField()
    updated_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'media'


class Platforms(models.Model):
    id = models.BigAutoField(primary_key=True)
    rawg_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=1024, blank=True, null=True)
    games_count = models.IntegerField(blank=True, null=True)
    oplay_games_count = models.IntegerField(blank=True, null=True)
    created_at = models.IntegerField()
    updated_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'platforms'


class PlatformsMapping(models.Model):
    id = models.BigAutoField(primary_key=True)
    platform = models.ForeignKey(Platforms, models.DO_NOTHING)
    game = models.ForeignKey(Games, models.DO_NOTHING)
    updated_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'platforms_mapping'


class SimilarGames(models.Model):
    id = models.BigAutoField(primary_key=True)
    game = models.ForeignKey(Games, models.DO_NOTHING)
    similar_game_id = models.BigIntegerField()
    updated_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'similar_games'


class StoreUpdates(models.Model):
    game_id = models.IntegerField()
    source = models.CharField(max_length=5)
    last_run = models.IntegerField()
    store_update_timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'store_updates'


class Stores(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    slug = models.CharField(max_length=64)
    link = models.CharField(max_length=255, blank=True, null=True)
    rawg_id = models.IntegerField(blank=True, null=True)
    cheapshark_id = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.IntegerField()
    updated_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stores'


class SystemRequirements(models.Model):
    id = models.BigAutoField(primary_key=True)
    platform_id = models.BigIntegerField()
    requirement = models.TextField()
    game = models.ForeignKey(Games, models.DO_NOTHING)
    created_at = models.IntegerField()
    updated_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'system_requirements'
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
