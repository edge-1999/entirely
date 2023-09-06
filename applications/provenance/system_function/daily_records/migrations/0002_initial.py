# Generated by Django 4.1 on 2023-06-02 18:12

from django.db import migrations
import django.db.models.deletion
import simplepro.components.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("daily_records", "0001_initial"),
        ("personal_Information", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="provenancesystemfunctiondailyrecordsevent",
            name="ID_PERSON",
            field=simplepro.components.fields.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="personal_Information.transactionsocialcultureethnicpopulationpersonalinformationperson",
                verbose_name="记录人员",
            ),
        ),
        migrations.AddField(
            model_name="provenancesystemfunctiondailyrecordsdiary",
            name="ID_PERSON",
            field=simplepro.components.fields.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="personal_Information.transactionsocialcultureethnicpopulationpersonalinformationperson",
                verbose_name="记录人员",
            ),
        ),
    ]
