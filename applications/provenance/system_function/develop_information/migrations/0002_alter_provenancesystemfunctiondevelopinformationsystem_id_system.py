# Generated by Django 4.1 on 2023-08-24 08:52

from django.db import migrations
import django.db.models.deletion
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        ("develop_information", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="provenancesystemfunctiondevelopinformationsystem",
            name="ID_SYSTEM",
            field=simplepro.components.fields.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="develop_information.provenancesystemfunctiondevelopinformationsystem",
                verbose_name="所属主机",
            ),
        ),
    ]
