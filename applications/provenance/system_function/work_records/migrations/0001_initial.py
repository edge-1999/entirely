# Generated by Django 4.1 on 2023-07-11 22:07

from django.db import migrations, models
import django.db.models.deletion
import simplepro.components.fields
import simplepro.editor.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("standard_encoding", "0001_initial"),
        (
            "organizations",
            "0005_alter_transactioneconomyindustryorganizationscertificate_date_end_and_more",
        ),
        (
            "account_management",
            "0009_provenancesystemsettingsaccountmanagementpermissionmenudisplay_id_display_and_more",
        ),
        ("project_server", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProvenanceSystemFunctionWorkRecordsOrganizations",
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
                    "ID_ORGANIZATIONS",
                    simplepro.components.fields.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organizations.transactioneconomyindustryorganizationsbases",
                        verbose_name="组织",
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
                "verbose_name": "账户所属组织",
                "verbose_name_plural": "账户所属组织",
                "db_table": "ProvenanceSystemFunctionWorkRecordsOrganizations",
                "ordering": ["-CREATE_TIME"],
            },
        ),
        migrations.CreateModel(
            name="ProvenanceSystemFunctionWorkRecordsProducts",
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
                    "ACCOUNT",
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
                (
                    "ACCOUNT_IDENTITY",
                    simplepro.components.fields.CharField(
                        blank=True, max_length=255, null=True, verbose_name="账户身份"
                    ),
                ),
                (
                    "AFFILIATED_PERSONNEL",
                    simplepro.components.fields.CharField(
                        blank=True, max_length=255, null=True, verbose_name="所属人员"
                    ),
                ),
                (
                    "DETAIL",
                    simplepro.editor.fields.MDTextField(
                        blank=True, null=True, verbose_name="详情描述"
                    ),
                ),
                (
                    "ID_WORK_RECORDS",
                    simplepro.components.fields.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="work_records.provenancesystemfunctionworkrecordsorganizations",
                        verbose_name="账户组织",
                    ),
                ),
                (
                    "PROJECT_SERVER_ID",
                    simplepro.components.fields.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="project_server.transactioneconomyindustryproductsprojectserver",
                        verbose_name="服务器",
                    ),
                ),
                (
                    "SERVER_ENVIRONMENT",
                    simplepro.components.fields.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="服务器环境",
                        to="standard_encoding.provenancesystemsettingsstandardcodemaindict",
                        verbose_name="服务器环境",
                    ),
                ),
            ],
            options={
                "verbose_name": "账户所属组织",
                "verbose_name_plural": "账户所属组织",
                "db_table": "ProvenanceSystemFunctionWorkRecordsProducts",
                "ordering": ["-CREATE_TIME"],
            },
        ),
    ]
