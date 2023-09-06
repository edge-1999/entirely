# Generated by Django 4.1 on 2023-07-31 09:29

from django.db import migrations, models
import django.db.models.deletion
import simplepro.components.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        (
            "data_records",
            "0004_alter_provenancesystemfunctiondatarecordssystem_id_subscriber",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="ProvenanceSystemFunctionDataRecordsTagTitle",
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
                        max_length=255, verbose_name="主题名称"
                    ),
                ),
                (
                    "ID_FOLDER",
                    simplepro.components.fields.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data_records.provenancesystemfunctiondatarecordssystemfolder",
                        verbose_name="工作目录",
                    ),
                ),
            ],
            options={
                "verbose_name": "标签主题",
                "verbose_name_plural": "标签主题",
                "db_table": "ProvenanceSystemFunctionDataRecordsTagTitle",
                "ordering": ["-CREATE_TIME"],
                "unique_together": {("ID_FOLDER", "NAME")},
            },
        ),
        migrations.RemoveField(
            model_name="provenancesystemfunctiondatarecordssystemfileobject",
            name="ID",
        ),
        migrations.AddField(
            model_name="provenancesystemfunctiondatarecordssystemfileobject",
            name="ID_PARENT",
            field=simplepro.components.fields.TreeComboboxField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="data_records.provenancesystemfunctiondatarecordssystemfileobject",
                verbose_name="上级",
            ),
        ),
        migrations.AlterField(
            model_name="provenancesystemfunctiondatarecordsfileobjecttag",
            name="ID_FILE_OBJECT",
            field=simplepro.components.fields.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="data_records.provenancesystemfunctiondatarecordssystemfileobject",
                verbose_name="文件对象",
            ),
        ),
        migrations.AlterField(
            model_name="provenancesystemfunctiondatarecordsfileobjecttag",
            name="ID_TAG",
            field=simplepro.components.fields.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="data_records.provenancesystemfunctiondatarecordstag",
                verbose_name="标签",
            ),
        ),
        migrations.AddField(
            model_name="provenancesystemfunctiondatarecordssystemfileobject",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=1,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="ProvenanceSystemFunctionDataRecordsTagTitleTag",
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
                    "ID_TAG",
                    simplepro.components.fields.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data_records.provenancesystemfunctiondatarecordstag",
                        verbose_name="标签",
                    ),
                ),
                (
                    "ID_TAG_TITLE",
                    simplepro.components.fields.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data_records.provenancesystemfunctiondatarecordstagtitle",
                        verbose_name="主题",
                    ),
                ),
            ],
            options={
                "verbose_name": "主题关联标签",
                "verbose_name_plural": "主题关联标签",
                "db_table": "ProvenanceSystemFunctionDataRecordsTagTitleTag",
                "ordering": ["-CREATE_TIME"],
                "unique_together": {("ID_TAG_TITLE", "ID_TAG")},
            },
        ),
    ]
