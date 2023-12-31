# Generated by Django 4.1 on 2023-06-12 14:10

from django.db import migrations, models
import django.db.models.deletion
import simplepro.components.fields
import simplepro.editor.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("standard_encoding", "0001_initial"),
        (
            "account_management",
            "0002_rename_id_provenancesystemsettingsaccountmanagementsuper_id",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="ProvenanceSystemSettingsAccountManagementSubscriber",
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
                    "NAME",
                    simplepro.components.fields.CharField(
                        blank=True, max_length=255, null=True, verbose_name="账户"
                    ),
                ),
                (
                    "PASSWORD",
                    simplepro.components.fields.CharField(
                        blank=True, max_length=255, null=True, verbose_name="密码"
                    ),
                ),
            ],
            options={
                "verbose_name": "订阅用户",
                "verbose_name_plural": "订阅用户",
                "db_table": "ProvenanceSystemSettingsAccountManagementSubscriber",
                "ordering": ["-CREATE_TIME"],
            },
        ),
        migrations.CreateModel(
            name="ProvenanceSystemSettingsAccountManagementSubscriberGroup",
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
                    "NAME",
                    simplepro.components.fields.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        unique=True,
                        verbose_name="账户",
                    ),
                ),
                (
                    "DETAIL",
                    simplepro.editor.fields.MDTextField(
                        blank=True, default=None, null=True, verbose_name="详细说明"
                    ),
                ),
                (
                    "ID_PARENT",
                    simplepro.components.fields.TreeComboboxField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account_management.provenancesystemsettingsaccountmanagementsubscribergroup",
                        verbose_name="上级",
                    ),
                ),
                (
                    "ID_SUBSCRIBER",
                    simplepro.components.fields.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account_management.provenancesystemsettingsaccountmanagementsubscriber",
                        verbose_name="订阅用户",
                    ),
                ),
            ],
            options={
                "verbose_name": "订阅用户组",
                "verbose_name_plural": "订阅用户组",
                "db_table": "ProvenanceSystemSettingsAccountManagementSubscriberGroup",
                "ordering": ["-CREATE_TIME"],
            },
        ),
        migrations.CreateModel(
            name="ProvenanceSystemSettingsAccountManagementRole",
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
                    "NAME",
                    simplepro.components.fields.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        unique=True,
                        verbose_name="角色名称",
                    ),
                ),
                (
                    "ID_PARENT",
                    simplepro.components.fields.TreeComboboxField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account_management.provenancesystemsettingsaccountmanagementrole",
                        verbose_name="上级",
                    ),
                ),
            ],
            options={
                "verbose_name": "角色管理",
                "verbose_name_plural": "角色管理",
                "db_table": "ProvenanceSystemSettingsAccountManagementRole",
                "ordering": ["-CREATE_TIME"],
            },
        ),
        migrations.CreateModel(
            name="ProvenanceSystemSettingsAccountManagementAuthority",
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
                    "NAME",
                    simplepro.components.fields.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        unique=True,
                        verbose_name="权限名称",
                    ),
                ),
                (
                    "ID_PARENT",
                    simplepro.components.fields.TreeComboboxField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account_management.provenancesystemsettingsaccountmanagementrole",
                        verbose_name="上级",
                    ),
                ),
            ],
            options={
                "verbose_name": "权限管理",
                "verbose_name_plural": "权限管理",
                "db_table": "ProvenanceSystemSettingsAccountManagementAuthority",
                "ordering": ["-CREATE_TIME"],
            },
        ),
        migrations.CreateModel(
            name="ProvenanceSystemSettingsAccountManagementSubscriberLand",
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
                    "UNIQUE_NUMBER",
                    simplepro.components.fields.CharField(
                        blank=True, max_length=255, null=True, verbose_name="账号"
                    ),
                ),
                (
                    "CODE",
                    simplepro.components.fields.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="standard_encoding.provenancesystemsettingsstandardcodemaindict",
                        verbose_name="关联登陆",
                    ),
                ),
                (
                    "ID_SUBSCRIBER",
                    simplepro.components.fields.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account_management.provenancesystemsettingsaccountmanagementsubscriber",
                        verbose_name="订阅用户",
                    ),
                ),
            ],
            options={
                "verbose_name": "关联登陆",
                "verbose_name_plural": "关联登陆",
                "db_table": "ProvenanceSystemSettingsAccountManagementSubscriberLand",
                "ordering": ["-CREATE_TIME"],
                "unique_together": {("ID_SUBSCRIBER", "UNIQUE_NUMBER", "CODE")},
            },
        ),
        migrations.CreateModel(
            name="ProvenanceSystemSettingsAccountManagementPermissionResults",
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
                    "ID_AUTHORITY",
                    simplepro.components.fields.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account_management.provenancesystemsettingsaccountmanagementauthority",
                        verbose_name="权限",
                    ),
                ),
                (
                    "ID_ROLE",
                    simplepro.components.fields.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account_management.provenancesystemsettingsaccountmanagementrole",
                        verbose_name="角色",
                    ),
                ),
                (
                    "ID_SUBSCRIBER",
                    simplepro.components.fields.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account_management.provenancesystemsettingsaccountmanagementsubscriber",
                        verbose_name="用户",
                    ),
                ),
                (
                    "ID_SUBSCRIBER_GROUP",
                    simplepro.components.fields.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account_management.provenancesystemsettingsaccountmanagementsubscribergroup",
                        verbose_name="用户组",
                    ),
                ),
            ],
            options={
                "verbose_name": "权限结果",
                "verbose_name_plural": "权限结果",
                "db_table": "ProvenanceSystemSettingsAccountManagementPermissionResults",
                "ordering": ["-CREATE_TIME"],
                "unique_together": {
                    ("ID_AUTHORITY", "ID_SUBSCRIBER", "ID_SUBSCRIBER_GROUP", "ID_ROLE")
                },
            },
        ),
    ]
