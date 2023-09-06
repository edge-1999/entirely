from django.db import models
from simplepro.components import fields
from simplepro.editor import fields as editor_fields

from docs.utils.model_communal.model_communal import BasesModelCommunalId
from docs.utils.model_communal.model_queryset import (
    get_queryset_function_products_type, get_queryset_function_organization_category_code,
    get_queryset_function_products_server_environment, get_queryset_function_products_products_project_correlation
)
from docs.utils.model_communal.model_values_filter import select_products_detail


# 产品基本信息
class TransactionEconomyIndustryProductsBasis(BasesModelCommunalId):
    """产品基本信息"""
    PRODUCTS_NAME = fields.CharField(
        verbose_name='产品名称', max_length=255, blank=True, null=True, show_word_limit=True)
    PRODUCTS_URL = models.URLField(verbose_name='网站链接', null=True, blank=True)
    DETAIL = editor_fields.MDTextField(verbose_name="详情描述", default=select_products_detail(), blank=True, null=True)

    class Meta:
        db_table = "TransactionEconomyIndustryProductsBasis"
        ordering = ['-CREATE_TIME']
        verbose_name = "产品基本信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.PRODUCTS_NAME}'


# 产品所属组织
class TransactionEconomyIndustryProductsAffiliation(BasesModelCommunalId):
    """产品所属组织"""
    ID_PRODUCTS = fields.ForeignKey(
        'products.TransactionEconomyIndustryProductsBasis', verbose_name='产品', on_delete=models.CASCADE, null=True,
        blank=True, to_field='ID', clearable=True, placeholder='产品')
    ID_ORGANIZATIONS = fields.ForeignKey(
        'organizations.TransactionEconomyIndustryOrganizationsBases', verbose_name='组织', on_delete=models.CASCADE,
        null=True, blank=True, to_field='ID', clearable=True, placeholder='组织', )

    class Meta:
        db_table = "TransactionEconomyIndustryProductsAffiliation"
        ordering = ['-CREATE_TIME']
        verbose_name = "产品所属组织"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_PRODUCTS}:{self.ID_ORGANIZATIONS}'


# 产品类型
class TransactionEconomyIndustryProductsType(BasesModelCommunalId):
    """产品类型"""
    ID_PRODUCTS = fields.ForeignKey(
        'products.TransactionEconomyIndustryProductsBasis', verbose_name='产品', on_delete=models.CASCADE, null=True,
        blank=True, to_field='ID', clearable=True, placeholder='产品')
    PRODUCTS_CODE = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='产品类型',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='产品类型',
        queryset=get_queryset_function_products_type, )

    class Meta:
        db_table = "TransactionEconomyIndustryProductsType"
        ordering = ['-CREATE_TIME']
        verbose_name = "产品类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_PRODUCTS}:{self.PRODUCTS_CODE}'


# 产品称呼信息
class TransactionEconomyIndustryProductsCall(BasesModelCommunalId):
    """产品称呼信息"""
    ID_PRODUCTS = fields.ForeignKey(
        'products.TransactionEconomyIndustryProductsBasis', verbose_name='产品', on_delete=models.CASCADE, null=True,
        blank=True, to_field='ID', clearable=True, placeholder='产品')
    NAME_CODE = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='称呼类型',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='称呼类型',
        queryset=get_queryset_function_organization_category_code, )
    NAME = fields.CharField(verbose_name='名称', max_length=255, blank=False, null=False, show_word_limit=True)

    class Meta:
        db_table = "TransactionEconomyIndustryProductsCall"
        ordering = ['-CREATE_TIME']
        verbose_name = "产品称呼信息"
        verbose_name_plural = verbose_name
        unique_together = ('ID_PRODUCTS', 'NAME_CODE', 'NAME')

    def __str__(self):
        return f'{self.ID_PRODUCTS}'


# 产品服务器
class TransactionEconomyIndustryProductsProductsServer(BasesModelCommunalId):
    """产品对应的服务器信息"""
    ID_PRODUCTS = fields.ForeignKey(
        'products.TransactionEconomyIndustryProductsBasis', verbose_name='产品', on_delete=models.CASCADE, null=True,
        blank=True, to_field='ID', clearable=True, placeholder='产品')
    PROJECT_SERVER_ID = fields.ForeignKey(
        'project_server.TransactionEconomyIndustryProductsProjectServer', verbose_name='服务器',
        on_delete=models.CASCADE, null=True, blank=True, to_field='ID', clearable=True, placeholder='服务器')
    SERVER_PROT = fields.CharField(
        verbose_name='服务器端口', max_length=10, blank=True, null=True, show_word_limit=True)
    SERVER_ENVIRONMENT = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='服务器环境',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='服务器环境',
        queryset=get_queryset_function_products_server_environment, related_name='产品服务器环境')
    DETAIL = editor_fields.MDTextField(verbose_name="详情描述", blank=True, null=True)

    class Meta:
        db_table = "TransactionEconomyIndustryProductsProductsServer"
        ordering = ['-CREATE_TIME']
        verbose_name = "产品服务器"
        verbose_name_plural = verbose_name
        unique_together = ('ID_PRODUCTS', 'PROJECT_SERVER_ID', 'SERVER_PROT', 'SERVER_ENVIRONMENT')

    def __str__(self):
        return f'{self.ID_PRODUCTS}:{self.SERVER_ENVIRONMENT}'


# 产品服务器账户
class TransactionEconomyIndustryProductsProductsServerAccount(BasesModelCommunalId):
    """产品服务器账户"""
    ID_PRODUCTS_SERVER = fields.ForeignKey(
        'products.TransactionEconomyIndustryProductsProductsServer', verbose_name='产品服务器',
        on_delete=models.CASCADE, null=True, blank=True, to_field='ID', clearable=True, placeholder='产品服务器')
    ACCOUNT = fields.CharField(verbose_name='账户', max_length=255, blank=True, null=True, show_word_limit=True)
    PASSWORD = fields.CharField(verbose_name='密码', max_length=255, blank=True, null=True, show_password=True)
    ACCOUNT_IDENTITY = fields.CharField(
        verbose_name='账户身份', max_length=255, blank=True, null=True, show_word_limit=True)
    AFFILIATED_PERSONNEL = fields.CharField(
        verbose_name='所属人员', max_length=255, blank=True, null=True, show_word_limit=True)
    DETAIL = editor_fields.MDTextField(verbose_name="详情描述", blank=True, null=True)

    class Meta:
        db_table = "TransactionEconomyIndustryProductsProductsServerAccount"
        ordering = ['-CREATE_TIME']
        verbose_name = "产品服务器账户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_PRODUCTS_SERVER}{self.ACCOUNT}'


# 项目对应产品
class TransactionEconomyIndustryProductsProductsProject(BasesModelCommunalId):
    """项目对应产品"""
    ID_PROJECT = fields.ForeignKey(
        'project.TransactionEconomyIndustryProductsProjectBasis', verbose_name='项目', on_delete=models.CASCADE,
        null=True, blank=True, to_field='ID', clearable=True, placeholder='项目', )
    ID_PRODUCTS = fields.ForeignKey(
        'products.TransactionEconomyIndustryProductsBasis', verbose_name='产品', on_delete=models.CASCADE, null=True,
        blank=True, to_field='ID', clearable=True, placeholder='产品')
    CORRELATION_CODE = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='关联',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='关联',
        queryset=get_queryset_function_products_products_project_correlation, )
    DETAIL = editor_fields.MDTextField(verbose_name="详情描述", blank=True, null=True)

    class Meta:
        db_table = "TransactionEconomyIndustryProductsProductsProject"
        ordering = ['-CREATE_TIME']
        verbose_name = "项目对应产品"
        verbose_name_plural = verbose_name
        unique_together = ('ID_PROJECT', 'ID_PRODUCTS', 'CORRELATION_CODE')

    def __str__(self):
        return f'{self.ID_PROJECT}{self.CORRELATION_CODE}的{self.ID_PRODUCTS}'
