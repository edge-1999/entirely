# Generated by Django 4.1 on 2023-07-11 13:51

from django.db import migrations, models
import django.db.models.deletion
import simplepro.components.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        (
            "organizations",
            "0004_alter_transactioneconomyindustryorganizationsbases_country_create_time_and_more",
        ),
        ("project", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transactioneconomyindustryproductsprojectbasis",
            name="PROJECT_CREATION_TIME",
            field=simplepro.components.fields.DateField(
                blank=True,
                default="2023-07-11 13:51:28",
                null=True,
                verbose_name="项目开始时间",
            ),
        ),
        migrations.AlterField(
            model_name="transactioneconomyindustryproductsprojectbasis",
            name="PROJECT_END_TIME",
            field=simplepro.components.fields.DateField(
                blank=True,
                default="2023-07-11 13:51:28",
                null=True,
                verbose_name="项目结束时间",
            ),
        ),
        migrations.CreateModel(
            name="TransactionEconomyIndustryProductsProjectOrganization",
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
                    "PROPORTION",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=4,
                        null=True,
                        verbose_name="占比%",
                    ),
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
                    "ID_PROJECT",
                    simplepro.components.fields.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="project.transactioneconomyindustryproductsprojectbasis",
                        verbose_name="项目",
                    ),
                ),
            ],
            options={
                "verbose_name": "项目所属组织",
                "verbose_name_plural": "项目所属组织",
                "db_table": "TransactionEconomyIndustryProductsProjectOrganization",
                "ordering": ["-CREATE_TIME"],
            },
        ),
    ]