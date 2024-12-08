
class DynamicDatabaseRouter:
    """
    This router directs all database operations for dynamically created models to the appropriate database.
    """

    def db_for_read(self, model, **hints):
        """
        Returns the database alias to use for reading operations on the given model.
        """
        # Check if the model is dynamically created or if it's an app model
        if hasattr(model, 'Meta') and hasattr(model.Meta, 'app_label'):
            app_label = model.Meta.app_label
            # Use the database alias that you associate with this app
            return self.get_database_for_app(app_label)
        return None  # Let Django decide if no dynamic model is involved

    def db_for_write(self, model, **hints):
        """
        Returns the database alias to use for writing operations on the given model.
        """
        # Similar to db_for_read, specify the database alias for writing
        if hasattr(model, 'Meta') and hasattr(model.Meta, 'app_label'):
            app_label = model.Meta.app_label
            return self.get_database_for_app(app_label)
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Determines if a relation between obj1 and obj2 should be allowed.
        """
        db_obj1 = router.db_for_read(obj1.__class__)
        db_obj2 = router.db_for_read(obj2.__class__)
        if db_obj1 == db_obj2:
            return True  # Relations are allowed within the same database
        return False  # Disallow relations across different databases

    def get_database_for_app(self, app_label):
        """
        Maps app labels to specific databases. This should return the database alias for the given app.
        """
        # Example mapping. Adjust this based on your project setup.
        app_to_db_map = {
            'app_name_1': 'db_1',  # Map app_name_1 to db_1
            'app_name_2': 'db_2',  # Map app_name_2 to db_2
        }
        return app_to_db_map.get(app_label, 'default')  # Default to 'default' if not specified
