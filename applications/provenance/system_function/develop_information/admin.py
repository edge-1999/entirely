from django.contrib import admin
from import_export import resources

from develop_information.models import (
    ProvenanceSystemFunctionDevelopInformationSystem,
    ProvenanceSystemFunctionDevelopInformationSystemService, ProvenanceSystemFunctionDevelopInformationSystemServiceProt
)
from docs.utils.admin_communal.admin_filter_obj import (
    ProvenanceSystemFunctionDevelopInformationSystemAdminSystemCategory,
    ProvenanceSystemFunctionDevelopInformationSystemAdminSystemArchitecture
)


@admin.register(ProvenanceSystemFunctionDevelopInformationSystem)
class ProvenanceSystemFunctionDevelopInformationSystemAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemFunctionDevelopInformationSystem

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = (
        'ID_PERSON', 'NAME', 'IP', 'SYSTEM_CATEGORY', 'ID_ORGANIZATIONS', 'IS_VIRTUAL_MACHINE',
        'ID_SYSTEM', 'ARCHITECTURE', 'ID_PRODUCTS',
    )
    search_fields = ('NAME', 'IP', 'DETAIL',)
    list_filter = (
        ProvenanceSystemFunctionDevelopInformationSystemAdminSystemCategory,
        'ID_ORGANIZATIONS', 'IS_VIRTUAL_MACHINE', 'ID_SYSTEM', 'ID_PRODUCTS', 'ID_PERSON',
        ProvenanceSystemFunctionDevelopInformationSystemAdminSystemArchitecture,
    )
    list_per_page = 10


@admin.register(ProvenanceSystemFunctionDevelopInformationSystemService)
class ProvenanceSystemFunctionDevelopInformationSystemServiceAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemFunctionDevelopInformationSystemService

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_SYSTEM', 'NAME', 'ID_PRODUCTS', 'ID_ORGANIZATIONS',)
    search_fields = ('NAME', 'DETAIL',)
    list_filter = ('ID_SYSTEM', 'ID_PRODUCTS', 'ID_ORGANIZATIONS',)
    list_per_page = 10


@admin.register(ProvenanceSystemFunctionDevelopInformationSystemServiceProt)
class ProvenanceSystemFunctionDevelopInformationSystemServiceProtAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemFunctionDevelopInformationSystemServiceProt

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_SYSTEM_SERVICE', 'PROT',)
    search_fields = ('PROT', 'DETAIL',)
    list_filter = ('ID_SYSTEM_SERVICE',)
    list_per_page = 10
