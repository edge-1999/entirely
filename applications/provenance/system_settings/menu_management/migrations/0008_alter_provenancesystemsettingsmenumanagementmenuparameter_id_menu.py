# Generated by Django 4.1 on 2023-07-20 18:08

from django.db import migrations
import django.db.models.deletion
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        (
            "menu_management",
            "0007_alter_provenancesystemsettingsmenumanagementmenuparameter_id_menu_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="provenancesystemsettingsmenumanagementmenuparameter",
            name="ID_MENU",
            field=simplepro.components.fields.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="menu_management.provenancesystemsettingsmenumanagementmenu",
                verbose_name="菜单",
            ),
        ),
    ]