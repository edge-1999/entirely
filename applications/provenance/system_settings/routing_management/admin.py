from django.contrib import admin
from import_export import resources

from routing_management.models import (
    ProvenanceSystemSettingsRoutingManagementNameSpace,
    ProvenanceSystemSettingsRoutingManagementNameSpaceName
)


@admin.register(ProvenanceSystemSettingsRoutingManagementNameSpace)
class ProvenanceSystemSettingsRoutingManagementNameSpaceAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemSettingsRoutingManagementNameSpace

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('NAME_SPACE', 'NAME',)
    search_fields = ('NAME_SPACE', 'NAME', 'DETAIL',)
    list_per_page = 10


@admin.register(ProvenanceSystemSettingsRoutingManagementNameSpaceName)
class ProvenanceSystemSettingsRoutingManagementNameSpaceNameAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemSettingsRoutingManagementNameSpaceName

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_NAME_SPACE', 'NAME_SPACE_NAME', 'NAME',)
    search_fields = ('NAME_SPACE_NAME', 'NAME', 'DETAIL',)
    list_filter = ('ID_NAME_SPACE',)
    list_per_page = 10
