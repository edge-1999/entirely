from django.contrib import admin
from import_export import resources

from docs.utils.admin_communal.admin_filter_obj import (
    TransactionEconomyIndustryProductsProjectServerAdminSystemCategory,
    TransactionEconomyIndustryProductsProjectServerAdminMirrorCategory,
    TransactionEconomyIndustryProductsProjectServerAdminInternetCategory
)
from project_server.models import TransactionEconomyIndustryProductsProjectServer


@admin.register(TransactionEconomyIndustryProductsProjectServer)
class TransactionEconomyIndustryProductsProjectServerAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionEconomyIndustryProductsProjectServer

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = (
        'NAME', 'PUBLIC_NETWORK', 'SYSTEM_CATEGORY', 'INSIDE_OUTSIDE_CODE')
    search_fields = ('NAME', 'INSTANCE_ID', 'PUBLIC_NETWORK', 'REGION',)
    list_filter = (
        TransactionEconomyIndustryProductsProjectServerAdminSystemCategory,
        TransactionEconomyIndustryProductsProjectServerAdminMirrorCategory,
        TransactionEconomyIndustryProductsProjectServerAdminInternetCategory
    )
    list_per_page = 10
