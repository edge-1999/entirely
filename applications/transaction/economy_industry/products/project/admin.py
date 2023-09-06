from django.contrib import admin
from import_export import resources

from project.models import (
    TransactionEconomyIndustryProductsProjectBasis,
    TransactionEconomyIndustryProductsProjectOrganization
)


@admin.register(TransactionEconomyIndustryProductsProjectBasis)
class TransactionEconomyIndustryProductsProjectBasisAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionEconomyIndustryProductsProjectBasis

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('PROJECT_NAME', 'PROJECT_CREATION_TIME', 'PROJECT_END_TIME',)
    search_fields = ('PROJECT_NAME', 'DETAIL',)
    list_filter = ('PROJECT_CREATION_TIME',)
    list_per_page = 10


@admin.register(TransactionEconomyIndustryProductsProjectOrganization)
class TransactionEconomyIndustryProductsProjectBasisAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionEconomyIndustryProductsProjectOrganization

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_PROJECT', 'ID_ORGANIZATIONS', 'PROPORTION',)
    list_filter = ('ID_PROJECT', 'ID_ORGANIZATIONS',)
    list_per_page = 10
