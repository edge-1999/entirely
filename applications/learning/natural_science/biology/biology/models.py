from django.db import models
from simplepro.components import fields

from docs.utils.model_communal.model_communal import BasesModelCommunal, BasesModelCommunalId
from docs.utils.model_communal.model_filter import get_combobox_queryset
from docs.utils.model_communal.model_queryset import (
    get_queryset_function_authority_type_data,
    get_queryset_function_call_code
)


class LearningNaturalScienceBiologicalSpecies(BasesModelCommunal):
    """生物种类"""
    NAME_CHINESE = fields.CharField(
        verbose_name='中文描述', max_length=255, blank=False, null=False, show_word_limit=True)
    STATUS_IS_EXTINCTION = models.BooleanField(verbose_name="是否灭绝", default=False, blank=False, null=False)
    MAN_MODE = models.BooleanField(verbose_name="人工培育", default=False, blank=False, null=False)
    ID_PARENT = fields.TreeComboboxField(
        'biology.LearningNaturalScienceBiologicalSpecies', on_delete=models.CASCADE, null=True, blank=True,
        verbose_name='上级', to_field='id', strictly=True, queryset=get_combobox_queryset, )
    STATUS_AUTHORITY = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='权限控制',
        on_delete=models.CASCADE, null=True, blank=True, clearable=True,
        placeholder='权限控制', queryset=get_queryset_function_authority_type_data, )

    class Meta:
        db_table = "LearningNaturalScienceBiologicalSpecies"
        ordering = ['-CREATE_TIME']
        verbose_name = "生物种类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.id}:{self.NAME_CHINESE}'


class LearningNaturalScienceBiologicalSpeciesCall(BasesModelCommunalId):
    """生物种类称呼"""
    ID_BIOLOGICAL_SPECIE = fields.ForeignKey(
        'biology.LearningNaturalScienceBiologicalSpecies', verbose_name='生物种类', on_delete=models.CASCADE,
        null=False, blank=False, to_field='id', clearable=True, placeholder='生物种类', )
    ENTERPRISE_NAME_CODE = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='生物种类类别',
        on_delete=models.CASCADE, null=False, blank=False, to_field='id', clearable=True, placeholder='生物种类类别',
        queryset=get_queryset_function_call_code, )
    ENTERPRISE_NAME = fields.CharField(
        verbose_name='名称', max_length=255, blank=False, null=False, show_word_limit=True)

    class Meta:
        db_table = "LearningNaturalScienceBiologicalSpeciesCall"
        ordering = ['-CREATE_TIME']
        verbose_name = "生物种类称呼"
        verbose_name_plural = verbose_name
        unique_together = ('ID_BIOLOGICAL_SPECIE', 'ENTERPRISE_NAME_CODE', 'ENTERPRISE_NAME')

    def __str__(self):
        return f'{self.ID_BIOLOGICAL_SPECIE}'
