from django.db import models
from simplepro.components import fields

from docs.utils.model_communal.model_communal import BasesModelCommunalId
from docs.utils.model_communal.model_queryset import (
    get_queryset_function_products_project_server,
    get_queryset_function_products_project_server_mirror_category,
    get_queryset_function_products_project_server_internet_category
)


# 服务器信息
class TransactionEconomyIndustryProductsProjectServer(BasesModelCommunalId):
    """服务器信息"""
    NAME = fields.CharField(verbose_name='服务器名称', max_length=255, blank=True, null=True, show_word_limit=True)
    INSTANCE_ID = fields.CharField(verbose_name='实例ID', max_length=255, blank=True, null=True, show_word_limit=True)
    PUBLIC_NETWORK = fields.CharField(verbose_name='公网IP', max_length=16, blank=True, null=True, show_word_limit=True)
    REGION = fields.CharField(verbose_name='地域', max_length=255, blank=True, null=True, show_word_limit=True)
    SYSTEM_CATEGORY = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='所属系统',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='所属系统',
        queryset=get_queryset_function_products_project_server, related_name='所属系统')
    MIRROR_CATEGORY = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='镜像名称',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='镜像名称',
        queryset=get_queryset_function_products_project_server_mirror_category, related_name='镜像名称')
    INSIDE_OUTSIDE_CODE = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='互联网类别',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='互联网类别',
        queryset=get_queryset_function_products_project_server_internet_category, related_name='互联网类别')

    class Meta:
        db_table = "TransactionEconomyIndustryProductsProjectServer"
        ordering = ['-CREATE_TIME']
        verbose_name = "服务器信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.NAME}({self.PUBLIC_NETWORK})'
