import time

from django.db import models
from simplepro.components import fields
from simplepro.editor import fields as editor_fields

from docs.utils.model_communal.model_communal import BasesModelCommunalId


# 项目基本信息
class TransactionEconomyIndustryProductsProjectBasis(BasesModelCommunalId):
    """项目基本信息"""
    PROJECT_NAME = fields.CharField(
        verbose_name='项目名称', max_length=255, blank=True, null=True, show_word_limit=True)
    PROJECT_CREATION_TIME = fields.DateField(
        verbose_name='项目开始时间', default=time.strftime("%Y-%m-%d %H:%M:%S"), blank=True, null=True, )
    PROJECT_END_TIME = fields.DateField(
        verbose_name='项目结束时间', default=time.strftime("%Y-%m-%d %H:%M:%S"), blank=True, null=True, )
    DETAIL = editor_fields.MDTextField(verbose_name="详情描述", blank=True, null=True, )

    class Meta:
        db_table = "TransactionEconomyIndustryProductsProjectBasis"
        ordering = ['-CREATE_TIME']
        verbose_name = "项目基本信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.PROJECT_NAME}{self.PROJECT_CREATION_TIME}'


# 项目所属组织
class TransactionEconomyIndustryProductsProjectOrganization(BasesModelCommunalId):
    """项目所属组织"""
    ID_PROJECT = fields.ForeignKey(
        'project.TransactionEconomyIndustryProductsProjectBasis', verbose_name='项目', on_delete=models.CASCADE,
        null=True, blank=True, to_field='ID', clearable=True, placeholder='项目', )
    ID_ORGANIZATIONS = fields.ForeignKey(
        'organizations.TransactionEconomyIndustryOrganizationsBases', verbose_name='组织', on_delete=models.CASCADE,
        null=True, blank=True, to_field='ID', clearable=True, placeholder='组织', )
    PROPORTION = models.DecimalField(verbose_name="占比%", decimal_places=2, max_digits=5, null=True, blank=True, )

    class Meta:
        db_table = "TransactionEconomyIndustryProductsProjectOrganization"
        ordering = ['-CREATE_TIME']
        verbose_name = "项目所属组织"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_PROJECT}{self.ID_ORGANIZATIONS}{self.PROPORTION}'
