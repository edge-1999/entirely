from django.contrib import admin
from import_export import resources

from docs.utils.admin_communal.admin_filter_obj import (
    ProvenanceSystemFunctionWorkRecordsProductsAdminServerEnvironment
)
from work_records.models import (
    ProvenanceSystemFunctionWorkRecordsOrganizations,
    ProvenanceSystemFunctionWorkRecordsProducts
)


@admin.register(ProvenanceSystemFunctionWorkRecordsOrganizations)
class ProvenanceSystemFunctionWorkRecordsOrganizationsAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemFunctionWorkRecordsOrganizations

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_SUBSCRIBER', 'ID_ORGANIZATIONS',)
    list_filter = ('ID_SUBSCRIBER', 'ID_ORGANIZATIONS',)
    list_per_page = 10


@admin.register(ProvenanceSystemFunctionWorkRecordsProducts)
class ProvenanceSystemFunctionWorkRecordsProductsAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemFunctionWorkRecordsProducts

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = (
        'ID_WORK_RECORDS', 'PROJECT_SERVER_ID', 'SERVER_ENVIRONMENT', 'ACCOUNT', 'PASSWORD', 'ACCOUNT_IDENTITY',
        'AFFILIATED_PERSONNEL',)
    search_fields = ('ACCOUNT', 'PASSWORD', 'ACCOUNT_IDENTITY', 'AFFILIATED_PERSONNEL', 'DETAIL',)
    list_filter = (
        'ID_WORK_RECORDS',
        'PROJECT_SERVER_ID',
        ProvenanceSystemFunctionWorkRecordsProductsAdminServerEnvironment
    )
    list_per_page = 10
