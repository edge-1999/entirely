# Generated by Django 4.1 on 2023-06-12 17:54

from django.db import migrations, models
import django.db.models.deletion
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        ("menu_management", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProvenanceSystemSettingsMenuManagementMenuParameter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "CREATE_TIME",
                    simplepro.components.fields.DateTimeField(
                        auto_now_add=True, verbose_name="创建时间"
                    ),
                ),
                (
                    "UPDATE_TIME",
                    models.DateTimeField(auto_now=True, verbose_name="更新时间"),
                ),
                (
                    "STATUS_IS_DELETE",
                    models.BooleanField(default=False, verbose_name="逻辑删除"),
                ),
                (
                    "STATUS_IS_EFFECTIVE",
                    models.BooleanField(default=True, verbose_name="是否有效"),
                ),
                (
                    "APP_URL_NAME",
                    simplepro.components.fields.CharField(
                        max_length=255, verbose_name="APP URL NAME"
                    ),
                ),
                (
                    "URL_NAME",
                    simplepro.components.fields.CharField(
                        max_length=255, verbose_name="URL NAME"
                    ),
                ),
                (
                    "ICON",
                    simplepro.components.fields.CharField(
                        max_length=255, verbose_name="图标"
                    ),
                ),
                (
                    "ID_MENU",
                    simplepro.components.fields.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="menu_management.provenancesystemsettingsmenumanagementmenu",
                        verbose_name="菜单",
                    ),
                ),
            ],
            options={
                "verbose_name": "菜单参数",
                "verbose_name_plural": "菜单参数",
                "db_table": "ProvenanceSystemSettingsMenuManagementMenuParameter",
                "ordering": ["-CREATE_TIME"],
            },
        ),
    ]
