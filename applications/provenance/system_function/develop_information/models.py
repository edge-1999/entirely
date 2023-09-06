from django.db import models
from simplepro.components import fields

from docs.utils.model_communal.model_communal import BasesModelCommunalIdCriterion
from docs.utils.model_communal.model_queryset import (
    get_queryset_project_server_code,
    get_queryset_project_system_architecture,
)


# Create your models here.
# 系统信息
class ProvenanceSystemFunctionDevelopInformationSystem(BasesModelCommunalIdCriterion):
    """系统信息"""
    ID_PERSON = fields.ForeignKey(
        'personal_Information.TransactionSocialCultureEthnicPopulationPersonalInformationPerson',
        verbose_name='人员', on_delete=models.CASCADE, null=False, blank=False, to_field='ID', clearable=True,
        placeholder='人员', )
    NAME = fields.CharField(verbose_name='系统名称', max_length=255, blank=True, null=True, show_word_limit=True)
    IP = fields.CharField(verbose_name='IP', max_length=16, blank=True, null=True, show_word_limit=True)
    SYSTEM_CATEGORY = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='所属系统',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='所属系统',
        queryset=get_queryset_project_server_code, related_name='系统信息_所属系统')
    ID_ORGANIZATIONS = fields.ForeignKey(
        'organizations.TransactionEconomyIndustryOrganizationsBases', verbose_name='组织', on_delete=models.CASCADE,
        null=True, blank=True, to_field='ID', clearable=True, placeholder='组织', )
    IS_VIRTUAL_MACHINE = models.BooleanField(verbose_name="是否虚拟机", default=False, blank=False, null=False)
    ID_SYSTEM = fields.ForeignKey(
        'develop_information.ProvenanceSystemFunctionDevelopInformationSystem', verbose_name='所属主机',
        on_delete=models.CASCADE, null=True, blank=True, to_field='ID', clearable=True, placeholder='所属主机', )
    ARCHITECTURE = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='系统架构',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='系统架构',
        queryset=get_queryset_project_system_architecture, related_name='系统信息_系统架构')
    ID_PRODUCTS = fields.ForeignKey(
        'products.TransactionEconomyIndustryProductsBasis', verbose_name='依托产品', on_delete=models.CASCADE,
        null=True, blank=True, to_field='ID', clearable=True, placeholder='依托产品')

    class Meta:
        db_table = "ProvenanceSystemFunctionDevelopInformationSystem"
        ordering = ['-CREATE_TIME']
        verbose_name = "系统信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.NAME}:{self.IP}'


# 系统服务信息
class ProvenanceSystemFunctionDevelopInformationSystemService(BasesModelCommunalIdCriterion):
    """系统服务信息"""
    ID_SYSTEM = fields.ForeignKey(
        'develop_information.ProvenanceSystemFunctionDevelopInformationSystem', verbose_name='所属主机',
        on_delete=models.CASCADE, null=False, blank=False, to_field='ID', clearable=True, placeholder='所属主机', )
    NAME = fields.CharField(verbose_name='服务名称', max_length=255, blank=True, null=True, show_word_limit=True)
    ID_PRODUCTS = fields.ForeignKey(
        'products.TransactionEconomyIndustryProductsBasis', verbose_name='依托产品', on_delete=models.CASCADE,
        null=True, blank=True, to_field='ID', clearable=True, placeholder='依托产品')
    ID_ORGANIZATIONS = fields.ForeignKey(
        'organizations.TransactionEconomyIndustryOrganizationsBases', verbose_name='所属组织', on_delete=models.CASCADE,
        null=True, blank=True, to_field='ID', clearable=True, placeholder='所属组织', )

    class Meta:
        db_table = "ProvenanceSystemFunctionDevelopInformationSystemService"
        ordering = ['-CREATE_TIME']
        verbose_name = "系统服务信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_SYSTEM}:{self.NAME}'


# 系统服务端口信息
class ProvenanceSystemFunctionDevelopInformationSystemServiceProt(BasesModelCommunalIdCriterion):
    """系统服务端口信息"""
    ID_SYSTEM_SERVICE = fields.ForeignKey(
        'develop_information.ProvenanceSystemFunctionDevelopInformationSystemService', verbose_name='系统服务',
        on_delete=models.CASCADE, null=False, blank=False, to_field='ID', clearable=True, placeholder='系统服务', )
    PROT = fields.CharField(verbose_name='端口', max_length=255, blank=True, null=True, show_word_limit=True)

    class Meta:
        db_table = "ProvenanceSystemFunctionDevelopInformationSystemServiceProt"
        ordering = ['-CREATE_TIME']
        verbose_name = "系统服务端口信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_SYSTEM_SERVICE}:{self.PROT}'
