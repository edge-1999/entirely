# Generated by Django 4.1 on 2023-06-28 13:03

from django.db import migrations, models
import django.db.models.deletion
import simplepro.components.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        (
            "account_management",
            "0008_alter_provenancesystemsettingsaccountmanagementauthority_code_and_more",
        ),
        (
            "menu_management",
            "0003_alter_provenancesystemsettingsmenumanagementmenuparameter_app_url_name_and_more",
        ),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="provenancesystemsettingsmenumanagementmenu",
            unique_together={("id", "ID_PARENT")},
        ),
        migrations.CreateModel(
            name="ProvenanceSystemSettingsMenuManagementMenuRoleDisplay",
            fields=[
                (
                    "ID",
                    models.UUIDField(
                        auto_created=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="标识",
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
                    "ID_MENU",
                    simplepro.components.fields.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="menu_management.provenancesystemsettingsmenumanagementmenu",
                        verbose_name="菜单",
                    ),
                ),
                (
                    "ID_ROLE",
                    simplepro.components.fields.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account_management.provenancesystemsettingsaccountmanagementrole",
                        verbose_name="角色",
                    ),
                ),
            ],
            options={
                "verbose_name": "菜单展示",
                "verbose_name_plural": "菜单展示",
                "db_table": "ProvenanceSystemSettingsMenuManagementMenuRoleDisplay",
                "ordering": ["-CREATE_TIME"],
                "unique_together": {("ID_ROLE", "ID_ROLE")},
            },
        ),
    ]
