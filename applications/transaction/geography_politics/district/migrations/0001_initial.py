# Generated by Django 4.1 on 2023-06-02 18:12

from django.db import migrations, models
import django.db.models.deletion
import simplepro.components.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("standard_encoding", "0001_initial"),
        ("country", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TransactionGeographyPoliticsDistrictBasic",
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
                    "NAME_CHINESE",
                    simplepro.components.fields.CharField(
                        blank=True, max_length=255, null=True, verbose_name="位置中文名称"
                    ),
                ),
                (
                    "NAME_ENGLISH",
                    simplepro.components.fields.CharField(
                        blank=True, max_length=255, null=True, verbose_name="位置英文名称"
                    ),
                ),
                (
                    "ID_SUBORDINATE",
                    simplepro.components.fields.CharField(
                        blank=True, max_length=255, null=True, verbose_name="位置编码"
                    ),
                ),
                (
                    "ID_NATION",
                    simplepro.components.fields.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="country.transactiongeographypoliticscountrycollect",
                        verbose_name="国家",
                    ),
                ),
                (
                    "ID_PARENT",
                    simplepro.components.fields.TreeComboboxField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="district.transactiongeographypoliticsdistrictbasic",
                        verbose_name="父级位置",
                    ),
                ),
                (
                    "TYPE_TOWN",
                    simplepro.components.fields.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="standard_encoding.provenancesystemsettingsstandardcodemaindict",
                        verbose_name="位置类别",
                    ),
                ),
            ],
            options={
                "verbose_name": "城镇信息",
                "verbose_name_plural": "城镇信息",
                "db_table": "TransactionGeographyPoliticsDistrictBasic",
                "ordering": ["-CREATE_TIME"],
            },
        ),
    ]
