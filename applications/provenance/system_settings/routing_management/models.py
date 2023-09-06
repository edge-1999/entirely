from django.db import models

from simplepro.components import fields
from simplepro.editor import fields as editor_fields

from docs.utils.model_communal.model_communal import BasesModelCommunalId


# 应用路由
class ProvenanceSystemSettingsRoutingManagementNameSpace(BasesModelCommunalId):
    """应用路由"""
    NAME_SPACE = fields.CharField(
        verbose_name='应用路由', max_length=255, blank=False, null=False, show_word_limit=True, unique=True)
    NAME = fields.CharField(verbose_name='中文描述', max_length=255, blank=False, null=False, show_word_limit=True)
    DETAIL = editor_fields.MDTextField(verbose_name="详情", blank=True, null=True)

    class Meta:
        db_table = "ProvenanceSystemSettingsRoutingManagementNameSpace"
        ordering = ['-CREATE_TIME']
        verbose_name = "应用路由"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.NAME_SPACE}'


# 应用子路由
class ProvenanceSystemSettingsRoutingManagementNameSpaceName(BasesModelCommunalId):
    """应用子路由"""
    ID_NAME_SPACE = fields.ForeignKey(
        'routing_management.ProvenanceSystemSettingsRoutingManagementNameSpace', verbose_name='应用路由',
        on_delete=models.CASCADE, null=False, blank=False, to_field='ID', clearable=True, placeholder='应用路由', )
    NAME_SPACE_NAME = fields.CharField(
        verbose_name='应用路由', max_length=255, blank=False, null=False, show_word_limit=True)
    NAME = fields.CharField(verbose_name='中文描述', max_length=255, blank=False, null=False, show_word_limit=True)
    DETAIL = editor_fields.MDTextField(verbose_name="详情", blank=True, null=True)

    class Meta:
        db_table = "ProvenanceSystemSettingsRoutingManagementNameSpaceName"
        ordering = ['-CREATE_TIME']
        verbose_name = "应用子路由"
        verbose_name_plural = verbose_name
        unique_together = ('ID_NAME_SPACE', 'NAME_SPACE_NAME',)

    def __str__(self):
        return f'{self.ID_NAME_SPACE}:{self.NAME_SPACE_NAME}'
