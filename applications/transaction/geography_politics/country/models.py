from django.db import models
from simplepro.components import fields
from simplepro.editor import fields as editor_fields
from docs.utils.model_communal.model_communal import BasesModelCommunalId
from docs.utils.model_communal.model_queryset import get_queryset_function_call_code


# 国家基本信息
class TransactionGeographyPoliticsCountryCollect(BasesModelCommunalId):
    """国家基本信息"""
    NAME = fields.CharField(
        verbose_name='国家名称', max_length=255, show_word_limit=True, blank=True, null=True)
    TWO_CHARACTER_CODE = fields.CharField(
        verbose_name='国家两字符代码', max_length=100, blank=True, null=True, show_word_limit=True)
    THREE_CHARACTER_CODE = fields.CharField(
        verbose_name='国家三字符代码', max_length=100, blank=True, null=True, show_word_limit=True)
    NUMERIC_CODE = fields.CharField(
        verbose_name='国家数字代码', max_length=100, blank=True, null=True, show_word_limit=True)

    class Meta:
        db_table = "TransactionGeographyPoliticsCountryCollect"
        ordering = ['-CREATE_TIME']
        verbose_name = "国家基本信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.NAME:
            return f'{self.NAME}'
        else:
            return f'{self.ID}'


# 国家称呼信息
class TransactionGeographyPoliticsCountryCollectCall(BasesModelCommunalId):
    """国家称呼信息"""
    ID_NATION = fields.ForeignKey(
        'country.TransactionGeographyPoliticsCountryCollect', verbose_name='国家', on_delete=models.CASCADE, null=False,
        blank=False, to_field='ID', clearable=True, placeholder='国家', )
    NAME_CODE = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='称呼类型',
        on_delete=models.CASCADE, null=False, blank=False, to_field='id', clearable=True, placeholder='称呼类型',
        queryset=get_queryset_function_call_code, )
    NAME = fields.CharField(verbose_name='名称', max_length=255, blank=False, null=False, show_word_limit=True)

    class Meta:
        db_table = "TransactionGeographyPoliticsCountryCollectCall"
        ordering = ['-CREATE_TIME']
        verbose_name = "国家称呼信息"
        verbose_name_plural = verbose_name
        unique_together = ('ID_NATION', 'NAME_CODE', 'NAME')

    def __str__(self):
        return f'{self.ID_NATION}'


class TransactionGeographyPoliticsCountryCurrency(BasesModelCommunalId):
    """国家货币"""
    ID_NATION = fields.ForeignKey(
        'country.TransactionGeographyPoliticsCountryCollect', verbose_name='国家', on_delete=models.CASCADE, null=True,
        blank=True, to_field='ID', clearable=True, placeholder='国家', )
    COUNTRY_DESCRIBE_CHINESE = fields.CharField(
        verbose_name='货币中文描述', max_length=100, blank=True, null=True, show_word_limit=True)
    COUNTRY_DESCRIBE_ENGLISH = fields.CharField(
        verbose_name='货币英文描述', max_length=100, blank=True, null=True, show_word_limit=True)
    COUNTRY_NOTATION = fields.CharField(
        verbose_name='货币符号', max_length=100, blank=True, null=True, show_word_limit=True)
    COUNTRY_ISO_CODE = fields.CharField(
        verbose_name='ISO代码', max_length=100, blank=True, null=True, show_word_limit=True)
    COUNTRY_AUXILIARY_UNIT = fields.CharField(
        verbose_name='辅助单位', max_length=100, blank=True, null=True, show_word_limit=True)
    COUNTRY_CARRY_SYSTEM = fields.CharField(
        verbose_name='进位制', max_length=100, blank=True, null=True, show_word_limit=True)
    DETAIL = editor_fields.MDTextField(verbose_name="备注", default=None, blank=True, null=True)

    class Meta:
        db_table = "TransactionGeographyPoliticsCountryCurrency"
        ordering = ['-CREATE_TIME']
        verbose_name = "国家货币"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.COUNTRY_DESCRIBE_CHINESE:
            return f'{self.ID_NATION}:{self.COUNTRY_DESCRIBE_CHINESE}'
        else:
            return f'{self.ID}'
