from django.contrib import admin
from import_export import resources

from data_records.models import (
    ProvenanceSystemFunctionDataRecordsSystem,
    ProvenanceSystemFunctionDataRecordsSystemFolder,
    ProvenanceSystemFunctionDataRecordsSystemFileObject,
    ProvenanceSystemFunctionDataRecordsTag,
    ProvenanceSystemFunctionDataRecordsFileObjectTag,
    ProvenanceSystemFunctionDataRecordsTagTitle,
    ProvenanceSystemFunctionDataRecordsTagTitleTag,
    ProvenanceSystemFunctionDataRecordsSystemFileObjectInherit
)
from docs.utils.admin_communal.admin_filter_obj import (
    ProvenanceSystemFunctionDataRecordsSystemAdminCode,
    ProvenanceSystemFunctionDataRecordsSystemFileObjectAdminType,
    ProvenanceSystemFunctionDataRecordsSystemFileObjectInheritType
)


@admin.register(ProvenanceSystemFunctionDataRecordsSystem)
class ProvenanceSystemFunctionDataRecordsSystemAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemFunctionDataRecordsSystem

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_SUBSCRIBER', 'ID_UNIQUE', 'SYSTEM_CATEGORY', 'NAME',)
    search_fields = ('ID_UNIQUE', 'NAME',)
    list_filter = ('ID_SUBSCRIBER', ProvenanceSystemFunctionDataRecordsSystemAdminCode,)
    list_per_page = 10


@admin.register(ProvenanceSystemFunctionDataRecordsSystemFolder)
class ProvenanceSystemFunctionDataRecordsSystemFolderAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemFunctionDataRecordsSystemFolder

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_SYSTEM', 'INODE', 'NAME', 'PATH',)
    search_fields = ('INODE', 'NAME', 'PATH',)
    list_filter = ('ID_SYSTEM',)
    list_per_page = 10


@admin.register(ProvenanceSystemFunctionDataRecordsSystemFileObject)
class ProvenanceSystemFunctionDataRecordsSystemFileObjectAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemFunctionDataRecordsSystemFileObject

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_PARENT', 'ID_FOLDER', 'INODE', 'NAME', 'PATH', 'TYPE',)
    search_fields = ('INODE', 'NAME', 'PATH',)
    list_filter = ('ID_FOLDER', ProvenanceSystemFunctionDataRecordsSystemFileObjectAdminType,)
    list_filter_tree = ('ID_PARENT',)
    list_per_page = 10

    # list_display_tree_cascade = 'ID_ASTRO_PARENT'
    # list_display_tree_expand_all = True  # 展开状态，默认不展开
    def get_list_filter_tree(self, request):
        return self.list_filter_tree

    def get_list_filter_tree_queryset(self, request, field_name):
        if field_name == 'ID_PARENT':
            return self.get_queryset(request)


@admin.register(ProvenanceSystemFunctionDataRecordsSystemFileObjectInherit)
class ProvenanceSystemFunctionDataRecordsSystemFileObjectInheritAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemFunctionDataRecordsSystemFileObjectInherit

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_FILE_OBJECT', 'INHERIT_TYPE', 'INHERIT_VALUE',)
    list_filter = ('ID_FILE_OBJECT', 'INHERIT_VALUE', ProvenanceSystemFunctionDataRecordsSystemFileObjectInheritType,)
    list_per_page = 10


@admin.register(ProvenanceSystemFunctionDataRecordsTagTitle)
class ProvenanceSystemFunctionDataRecordsTagTitleAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemFunctionDataRecordsTagTitle

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_FOLDER', 'NAME',)
    search_fields = ('NAME',)
    list_filter = ('ID_FOLDER',)
    list_per_page = 10


@admin.register(ProvenanceSystemFunctionDataRecordsTag)
class ProvenanceSystemFunctionDataRecordsTagAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemFunctionDataRecordsTag

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_FOLDER', 'NAME',)
    search_fields = ('NAME',)
    list_filter = ('ID_FOLDER',)
    list_per_page = 10


@admin.register(ProvenanceSystemFunctionDataRecordsTagTitleTag)
class ProvenanceSystemFunctionDataRecordsTagTitleTagAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemFunctionDataRecordsTagTitleTag

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_TAG_TITLE', 'ID_TAG',)
    list_filter = ('ID_TAG_TITLE', 'ID_TAG',)
    list_per_page = 10


@admin.register(ProvenanceSystemFunctionDataRecordsFileObjectTag)
class ProvenanceSystemFunctionDataRecordsFileObjectTagAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemFunctionDataRecordsFileObjectTag

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_TAG', 'ID_FILE_OBJECT',)
    list_filter = ('ID_TAG', 'ID_FILE_OBJECT',)
    list_per_page = 10
