from django.db import models
from simplepro.components import fields
from simplepro.editor import fields as editor_fields

from docs.utils.model_communal.model_communal import BasesModelCommunalId
from docs.utils.model_communal.model_queryset import get_queryset_function_products_server_environment


# 账户所属组织
class ProvenanceSystemFunctionWorkRecordsOrganizations(BasesModelCommunalId):
    """账户所属组织"""
    ID_SUBSCRIBER = fields.ForeignKey(
        'account_management.ProvenanceSystemSettingsAccountManagementSubscriber', verbose_name='订阅用户',
        on_delete=models.CASCADE, null=False, blank=False, to_field='ID', clearable=True, placeholder='订阅用户', )
    ID_ORGANIZATIONS = fields.ForeignKey(
        'organizations.TransactionEconomyIndustryOrganizationsBases', verbose_name='组织', on_delete=models.CASCADE,
        null=True, blank=True, to_field='ID', clearable=True, placeholder='组织', )

    class Meta:
        db_table = "ProvenanceSystemFunctionWorkRecordsOrganizations"
        ordering = ['-CREATE_TIME']
        verbose_name = "账户所属组织"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_SUBSCRIBER}-{self.ID_ORGANIZATIONS}'


# 组织产品账户密码
class ProvenanceSystemFunctionWorkRecordsProducts(BasesModelCommunalId):
    """产品所在的服务器账号密码"""
    ID_WORK_RECORDS = fields.ForeignKey(
        'work_records.ProvenanceSystemFunctionWorkRecordsOrganizations', verbose_name='账户组织',
        on_delete=models.CASCADE, null=True, blank=True, to_field='ID', clearable=True, placeholder='账户组织')
    PROJECT_SERVER_ID = fields.ForeignKey(
        'project_server.TransactionEconomyIndustryProductsProjectServer', verbose_name='服务器',
        on_delete=models.CASCADE, null=True, blank=True, to_field='ID', clearable=True, placeholder='服务器')
    SERVER_ENVIRONMENT = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='服务器环境',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='服务器环境',
        queryset=get_queryset_function_products_server_environment, related_name='服务器环境')
    ACCOUNT = fields.CharField(verbose_name='账户', max_length=255, blank=True, null=True, show_word_limit=True)
    PASSWORD = fields.CharField(verbose_name='密码', max_length=255, blank=True, null=True, show_password=True)
    ACCOUNT_IDENTITY = fields.CharField(
        verbose_name='账户身份', max_length=255, blank=True, null=True, show_word_limit=True)
    AFFILIATED_PERSONNEL = fields.CharField(
        verbose_name='所属人员', max_length=255, blank=True, null=True, show_word_limit=True)
    DETAIL = editor_fields.MDTextField(verbose_name="详情描述", blank=True, null=True)

    class Meta:
        db_table = "ProvenanceSystemFunctionWorkRecordsProducts"
        ordering = ['-CREATE_TIME']
        verbose_name = "账户所属组织"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_WORK_RECORDS}'
