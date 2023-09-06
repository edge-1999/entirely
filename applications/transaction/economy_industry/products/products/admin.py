from django.contrib import admin
from import_export import resources

from docs.utils.admin_communal.admin_filter_obj import (
    TransactionEconomyIndustryProductsTypeType,
    TransactionEconomyIndustryProductsCallAddressAdminCode,
    TransactionEconomyIndustryProductsProductsServerAdminServerEnvironment,
    TransactionEconomyIndustryProductsProductsProjectAdmin
)
from products.models import (
    TransactionEconomyIndustryProductsBasis,
    TransactionEconomyIndustryProductsAffiliation,
    TransactionEconomyIndustryProductsType,
    TransactionEconomyIndustryProductsCall,
    TransactionEconomyIndustryProductsProductsServer, TransactionEconomyIndustryProductsProductsServerAccount,
    TransactionEconomyIndustryProductsProductsProject
)


@admin.register(TransactionEconomyIndustryProductsBasis)
class TransactionEconomyIndustryProductsBasisAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionEconomyIndustryProductsBasis

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('PRODUCTS_NAME', 'PRODUCTS_URL',)
    search_fields = ('PRODUCTS_NAME', 'PRODUCTS_URL', 'DETAIL',)
    list_per_page = 10


@admin.register(TransactionEconomyIndustryProductsAffiliation)
class TransactionEconomyIndustryProductsAffiliationAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionEconomyIndustryProductsAffiliation

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_PRODUCTS', 'ID_ORGANIZATIONS',)
    list_filter = ('ID_PRODUCTS', 'ID_ORGANIZATIONS',)
    list_per_page = 10


@admin.register(TransactionEconomyIndustryProductsType)
class TransactionEconomyIndustryProductsTypeAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionEconomyIndustryProductsType

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_PRODUCTS', 'PRODUCTS_CODE',)
    list_filter = ('ID_PRODUCTS', TransactionEconomyIndustryProductsTypeType,)
    list_per_page = 10


@admin.register(TransactionEconomyIndustryProductsCall)
class TransactionEconomyIndustryProductsCallAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionEconomyIndustryProductsCall

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_PRODUCTS', 'NAME_CODE', 'NAME',)
    search_fields = ('NAME',)
    list_filter = ('ID_PRODUCTS', TransactionEconomyIndustryProductsCallAddressAdminCode,)
    list_per_page = 10


@admin.register(TransactionEconomyIndustryProductsProductsServer)
class TransactionEconomyIndustryProductsProductsServerAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionEconomyIndustryProductsProductsServer

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_PRODUCTS', 'PROJECT_SERVER_ID', 'SERVER_PROT', 'SERVER_ENVIRONMENT',)
    search_fields = ('DETAIL',)
    list_filter = (
        'ID_PRODUCTS', 'PROJECT_SERVER_ID',
        TransactionEconomyIndustryProductsProductsServerAdminServerEnvironment
    )
    list_per_page = 10


@admin.register(TransactionEconomyIndustryProductsProductsServerAccount)
class TransactionEconomyIndustryProductsProductsServerAccountAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionEconomyIndustryProductsProductsServerAccount

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_PRODUCTS_SERVER', 'ACCOUNT', 'PASSWORD', 'ACCOUNT_IDENTITY', 'AFFILIATED_PERSONNEL',)
    search_fields = ('ACCOUNT', 'PASSWORD', 'ACCOUNT_IDENTITY', 'AFFILIATED_PERSONNEL', 'DETAIL',)
    list_filter = ('ID_PRODUCTS_SERVER',)
    list_per_page = 10


@admin.register(TransactionEconomyIndustryProductsProductsProject)
class TransactionEconomyIndustryProductsProductsProjectAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionEconomyIndustryProductsProductsProject

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_PROJECT', 'ID_PRODUCTS', 'CORRELATION_CODE',)
    search_fields = ('DETAIL',)
    list_filter = ('ID_PROJECT', 'ID_PRODUCTS', TransactionEconomyIndustryProductsProductsProjectAdmin)
    list_per_page = 10
