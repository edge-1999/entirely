# Generated by Django 4.1 on 2023-07-21 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "menu_management",
            "0009_provenancesystemsettingsmenumanagementmenuparameter_name_space",
        ),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="provenancesystemsettingsmenumanagementmenuparameter",
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name="provenancesystemsettingsmenumanagementmenuparameter",
            name="APP_URL_NAME",
        ),
        migrations.RemoveField(
            model_name="provenancesystemsettingsmenumanagementmenuparameter",
            name="URL_NAME",
        ),
    ]