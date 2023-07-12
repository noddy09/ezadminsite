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


class GameDataMapper(models.Model):
    id = models.PositiveBigIntegerField()
    game = models.ForeignKey('Games', models.DO_NOTHING)
    store = models.ForeignKey('Stores', models.DO_NOTHING)
    filepath_mapper = models.JSONField()

    class Meta:
        managed = False
        db_table = 'game_data_mapper'


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
