# Generated by Django 4.1 on 2023-07-11 22:07

from django.db import migrations
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        (
            "organizations",
            "0004_alter_transactioneconomyindustryorganizationsbases_country_create_time_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="transactioneconomyindustryorganizationscertificate",
            name="DATE_END",
            field=simplepro.components.fields.DateField(
                blank=True,
                default="2023-07-11 22:07:23",
                null=True,
                verbose_name="组织证件号有效结束日期",
            ),
        ),
        migrations.AlterField(
            model_name="transactioneconomyindustryorganizationscertificate",
            name="DATE_ISSUED",
            field=simplepro.components.fields.DateField(
                blank=True,
                default="2023-07-11 22:07:23",
                null=True,
                verbose_name="签发日期",
            ),
        ),
        migrations.AlterField(
            model_name="transactioneconomyindustryorganizationscertificate",
            name="DATE_START",
            field=simplepro.components.fields.DateField(
                blank=True,
                default="2023-07-11 22:07:23",
                null=True,
                verbose_name="组织证件号有效开始日期",
            ),
        ),
    ]