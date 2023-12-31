# Generated by Django 4.1 on 2023-07-22 20:43

from django.db import migrations
import django.db.models.deletion
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        ("standard_encoding", "0001_initial"),
        ("country", "0002_transactiongeographypoliticscountrycollect_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="transactiongeographypoliticscountrycollect",
            name="CHINESE_ABBREVIATION",
        ),
        migrations.RemoveField(
            model_name="transactiongeographypoliticscountrycollect",
            name="ENGLISH_ABBREVIATION",
        ),
        migrations.RemoveField(
            model_name="transactiongeographypoliticscountrycollect",
            name="NAME_CHINA",
        ),
        migrations.RemoveField(
            model_name="transactiongeographypoliticscountrycollect",
            name="NAME_ENGLISH",
        ),
        migrations.AlterField(
            model_name="transactiongeographypoliticscountrycollectcall",
            name="ID_NATION",
            field=simplepro.components.fields.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="country.transactiongeographypoliticscountrycollect",
                verbose_name="国家",
            ),
        ),
        migrations.AlterField(
            model_name="transactiongeographypoliticscountrycollectcall",
            name="NAME_CODE",
            field=simplepro.components.fields.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="standard_encoding.provenancesystemsettingsstandardcodemaindict",
                verbose_name="称呼类型",
            ),
        ),
    ]
