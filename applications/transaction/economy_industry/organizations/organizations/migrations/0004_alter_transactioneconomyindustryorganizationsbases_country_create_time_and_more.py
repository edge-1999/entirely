# Generated by Django 4.1 on 2023-07-11 13:51

from django.db import migrations
import simplepro.components.fields
import simplepro.editor.fields


class Migration(migrations.Migration):

    dependencies = [
        (
            "organizations",
            "0003_alter_transactioneconomyindustryorganizationscertificate_date_end_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="transactioneconomyindustryorganizationsbases",
            name="COUNTRY_CREATE_TIME",
            field=simplepro.components.fields.DateField(
                blank=True, default="2023-07-11", null=True, verbose_name="成立时间"
            ),
        ),
        migrations.AlterField(
            model_name="transactioneconomyindustryorganizationsbases",
            name="COUNTRY_END_TIME",
            field=simplepro.components.fields.DateField(
                blank=True, default="2023-07-11", null=True, verbose_name="结束时间"
            ),
        ),
        migrations.AlterField(
            model_name="transactioneconomyindustryorganizationscertificate",
            name="DATE_END",
            field=simplepro.components.fields.DateField(
                blank=True,
                default="2023-07-11 13:51:28",
                null=True,
                verbose_name="组织证件号有效结束日期",
            ),
        ),
        migrations.AlterField(
            model_name="transactioneconomyindustryorganizationscertificate",
            name="DATE_ISSUED",
            field=simplepro.components.fields.DateField(
                blank=True,
                default="2023-07-11 13:51:28",
                null=True,
                verbose_name="签发日期",
            ),
        ),
        migrations.AlterField(
            model_name="transactioneconomyindustryorganizationscertificate",
            name="DATE_START",
            field=simplepro.components.fields.DateField(
                blank=True,
                default="2023-07-11 13:51:28",
                null=True,
                verbose_name="组织证件号有效开始日期",
            ),
        ),
        migrations.AlterField(
            model_name="transactioneconomyindustryorganizationsdetails",
            name="DETAIL",
            field=simplepro.editor.fields.MDTextField(
                blank=True,
                default="# 组织详细介绍\n\n## 企业的发展历程\n\n> 概述企业从成立到现在的发展历史、重要里程碑和关键事件。\n\n## 业务范围\n\n> 描述组织的主要业务领域、产品或服务类型。\n\n\n## 使命和价值观\n\n> 组织的使命宣言和核心价值观。\n\n\n## 经营模式和策略\n\n> 描述企业的经营模式、战略决策和业务发展方向。\n\n\n## 经营成果和业绩\n\n> 总结企业在过去的经营活动中取得的成就、销售收入、利润、市场份额等。\n\n\n## 组织历史\n\n> 组织的成立日期、重要里程碑、发展历程等。",
                null=True,
                verbose_name="详情描述",
            ),
        ),
    ]
