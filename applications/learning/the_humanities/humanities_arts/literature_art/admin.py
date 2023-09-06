from django.contrib import admin
from import_export import resources

from docs.utils.admin_communal.admin_filter_obj import (
    TransactionEconomyIndustryOrganizationsBasesAdminEnterprise, TransactionEconomyIndustryOrganizationsCallAdminCode,
    TransactionEconomyIndustryOrganizationsAddressAdminCode, TransactionEconomyIndustryOrganizationsCertificateCode,
    LearningTheHumanitiesHumanitiesArtsLiteratureArtContentTypeAdminType
)
from literature_art.models import LearningTheHumanitiesHumanitiesArtsLiteratureArtContent, \
    LearningTheHumanitiesHumanitiesArtsLiteratureArtContentType


@admin.register(LearningTheHumanitiesHumanitiesArtsLiteratureArtContent)
class LearningTheHumanitiesHumanitiesArtsLiteratureArtContentAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = LearningTheHumanitiesHumanitiesArtsLiteratureArtContent

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ("ID", 'CONTENT',)
    search_fields = ("ID", 'CONTENT',)
    list_per_page = 10


@admin.register(LearningTheHumanitiesHumanitiesArtsLiteratureArtContentType)
class LearningTheHumanitiesHumanitiesArtsLiteratureArtContentTypeAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = LearningTheHumanitiesHumanitiesArtsLiteratureArtContentType

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('LITERATURE_ART_CODE', 'LITERATURE_ART_ID',)
    list_filter = (LearningTheHumanitiesHumanitiesArtsLiteratureArtContentTypeAdminType, 'LITERATURE_ART_ID',)
    list_per_page = 10
