# Generated by Django 4.1 on 2023-06-12 15:09

from django.db import migrations
import django.db.models.deletion
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        (
            "account_management",
            "0003_provenancesystemsettingsaccountmanagementsubscriber_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="provenancesystemsettingsaccountmanagementpermissionresults",
            name="ID_AUTHORITY",
            field=simplepro.components.fields.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="account_management.provenancesystemsettingsaccountmanagementauthority",
                verbose_name="权限",
            ),
        ),
        migrations.AlterField(
            model_name="provenancesystemsettingsaccountmanagementpermissionresults",
            name="ID_ROLE",
            field=simplepro.components.fields.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="account_management.provenancesystemsettingsaccountmanagementrole",
                verbose_name="角色",
            ),
        ),
        migrations.AlterField(
            model_name="provenancesystemsettingsaccountmanagementpermissionresults",
            name="ID_SUBSCRIBER",
            field=simplepro.components.fields.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="account_management.provenancesystemsettingsaccountmanagementsubscriber",
                verbose_name="用户",
            ),
        ),
        migrations.AlterField(
            model_name="provenancesystemsettingsaccountmanagementpermissionresults",
            name="ID_SUBSCRIBER_GROUP",
            field=simplepro.components.fields.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="account_management.provenancesystemsettingsaccountmanagementsubscribergroup",
                verbose_name="用户组",
            ),
        ),
        migrations.AlterField(
            model_name="provenancesystemsettingsaccountmanagementsubscribergroup",
            name="ID_SUBSCRIBER",
            field=simplepro.components.fields.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="account_management.provenancesystemsettingsaccountmanagementsubscriber",
                verbose_name="订阅用户",
            ),
        ),
    ]
