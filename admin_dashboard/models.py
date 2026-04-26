from django.db import models


class AdminControl(models.Model):
    """
    Dummy model used only for defining custom permissions.
    """

    class Meta:
        permissions = [
            ("can_train_model", "Can train ML model"),
            ("can_view_dashboard", "Can view dashboard"),
            ("can_view_users", "Can view users"),
            ("can_view_predictions", "Can view predictions"),
            ("can_view_analytics", "Can view analytics"),
        ]