# Generated by Django 4.1 on 2023-06-12 17:57

from django.db import migrations
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        ("menu_management", "0002_provenancesystemsettingsmenumanagementmenuparameter"),
    ]

    operations = [
        migrations.AlterField(
            model_name="provenancesystemsettingsmenumanagementmenuparameter",
            name="APP_URL_NAME",
            field=simplepro.components.fields.CharField(
                blank=True, max_length=255, null=True, verbose_name="APP URL NAME"
            ),
        ),
        migrations.AlterField(
            model_name="provenancesystemsettingsmenumanagementmenuparameter",
            name="ICON",
            field=simplepro.components.fields.CharField(
                blank=True, max_length=255, null=True, verbose_name="图标"
            ),
        ),
        migrations.AlterField(
            model_name="provenancesystemsettingsmenumanagementmenuparameter",
            name="URL_NAME",
            field=simplepro.components.fields.CharField(
                blank=True, max_length=255, null=True, verbose_name="URL NAME"
            ),
        ),
    ]
