from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from standard_encoding.models import ProvenanceSystemSettingsStandardCodeMainDict


class TransactionGeographyPoliticsDistrictType(admin.SimpleListFilter):
    title = _('城镇分类')
    parameter_name = 'TransactionGeographyPoliticsDistrictType'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='PoliticsDistrictType').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        return queryset.filter(TYPE_TOWN=self.value())


class PermissionControlDataLearningNaturalScienceAstronomyCosmologyCode(admin.SimpleListFilter):
    title = _('权限控制-数据')
    parameter_name = 'PermissionControlDataLearningNaturalScienceAstronomyCosmologyCode'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='PermissionControlData').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(STATUS_AUTHORITY=self.value())


class ProvenanceSystemSettingsAccountManagementAuthorityAdminCode(admin.SimpleListFilter):
    title = _('权限控制-操作')
    parameter_name = 'ProvenanceSystemSettingsAccountManagementAuthorityAdminCode'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='PermissionControlMenu').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(CODE=self.value())


class TransactionSocialCultureEthnicPopulationPersonalInformationPersonAdminSex(admin.SimpleListFilter):
    title = _('生理性别')
    parameter_name = 'TransactionSocialCultureEthnicPopulationPersonalInformationPersonAdminSex'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='HumanPhysiologicalGender').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(SEX=self.value())


class TransactionSocialCultureEthnicPopulationPersonalInformationPersonBirthdayAdminBirthday(admin.SimpleListFilter):
    title = _('生日类别')
    parameter_name = 'TransactionSocialCultureEthnicPopulationPersonalInformationPersonAdminSex'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='Calendar').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(TYPE_BIRTHDAY=self.value())


class TransactionSocialCultureEthnicPopulationPersonalInformationPersonAddressAdminAddress(admin.SimpleListFilter):
    title = _('地址类别')
    parameter_name = 'TransactionSocialCultureEthnicPopulationPersonalInformationPersonAdminSex'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='PersonalAddress').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(TYPE_ADDRESS=self.value())


class TransactionSocialCultureEthnicPopulationPersonalInformationPersonEventAdminEvent(admin.SimpleListFilter):
    title = _('事件类型')
    parameter_name = 'TransactionSocialCultureEthnicPopulationPersonalInformationPersonAdminSex'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='PersonalEvent').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(RTYPE_EVENT=self.value())


class TransactionEconomyIndustryOrganizationsBasesAdminEnterprise(admin.SimpleListFilter):
    title = _('组织类别')
    parameter_name = 'TransactionEconomyIndustryOrganizationsBasesAdminEnterprise'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='OrganizationCategory').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(ENTERPRISE_CODE=self.value())


class TransactionEconomyIndustryOrganizationsCallAdminCode(admin.SimpleListFilter):
    title = _('组织称呼类型')
    parameter_name = 'TransactionEconomyIndustryOrganizationsCallAdminCode'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='OrganizationCategoryCode').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(ENTERPRISE_NAME_CODE=self.value())


class TransactionEconomyIndustryOrganizationsAddressAdminCode(admin.SimpleListFilter):
    title = _('组织称呼类型')
    parameter_name = 'TransactionEconomyIndustryOrganizationsAddressAdminCode'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='OrganizationAddressCode').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(ENTERPRISE_ADDRESS_CODE=self.value())


class TransactionEconomyIndustryProductsCallAddressAdminCode(admin.SimpleListFilter):
    title = _('产品称呼类型')
    parameter_name = 'TransactionEconomyIndustryProductsCallAddressAdminCode'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='OrganizationAddressCode').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(NAME_CODE=self.value())


class TransactionEconomyIndustryOrganizationsCertificateCode(admin.SimpleListFilter):
    title = _('组织证件信息')
    parameter_name = 'TransactionEconomyIndustryOrganizationsCertificateCode'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='OrganizationsCertificateCode').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(CODE=self.value())


class TransactionSocialCultureEthnicPopulationPersonalInformationPersonCertificateCode(admin.SimpleListFilter):
    title = _('个人证件信息')
    parameter_name = 'TransactionSocialCultureEthnicPopulationPersonalInformationPersonCertificateCode'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='PersonCertificateCode').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(CODE=self.value())


class TransactionEconomyIndustryProductsTypeType(admin.SimpleListFilter):
    title = _('产品类型')
    parameter_name = 'TransactionEconomyIndustryProductsTypeType'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='ProductsType').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(PRODUCTS_CODE=self.value())


class ProvenanceSystemFunctionDailyRecordsEventIdentity(admin.SimpleListFilter):
    title = _('事件参与身份')
    parameter_name = 'ProvenanceSystemFunctionDailyRecordsEventIdentity'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='RecordsEventIdentity').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(IDENTITY=self.value())


class ProvenanceSystemFunctionDailyRecordsEventTypeCode(admin.SimpleListFilter):
    title = _('事件类型')
    parameter_name = 'ProvenanceSystemFunctionDailyRecordsEventTypeCode'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='RecordsEventType').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(CODE=self.value())


class ProvenanceSystemFunctionPasswordRecordsAdminCode(admin.SimpleListFilter):
    title = _('产品关联类别')
    parameter_name = 'ProvenanceSystemFunctionPasswordRecordsAdminCode'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='PasswordCorrelationCode').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(CODE=self.value())


class ProvenanceSystemSettingsAccountManagementSubscriberLandAdminCode(admin.SimpleListFilter):
    title = _('关联登陆')
    parameter_name = 'ProvenanceSystemSettingsAccountManagementSubscriberLandAdminCode'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='SubscriberLandCode').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(CODE=self.value())


class TransactionEconomyIndustryProductsProjectServerAdminSystemCategory(admin.SimpleListFilter):
    title = _('所属系统')
    parameter_name = 'TransactionEconomyIndustryProductsProjectServerAdminSystemCategory'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='SystemCategory').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(SYSTEM_CATEGORY=self.value())


class TransactionEconomyIndustryProductsProjectServerAdminMirrorCategory(admin.SimpleListFilter):
    title = _('镜像名称')
    parameter_name = 'TransactionEconomyIndustryProductsProjectServerAdminMirrorCategory'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='MirrorCategory').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(MIRROR_CATEGORY=self.value())


class TransactionEconomyIndustryProductsProjectServerAdminInternetCategory(admin.SimpleListFilter):
    title = _('互联网类别')
    parameter_name = 'TransactionEconomyIndustryProductsProjectServerAdminMirrorCategory'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='InternetCategory').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(INSIDE_OUTSIDE_CODE=self.value())


class ProvenanceSystemFunctionWorkRecordsProductsAdminServerEnvironment(admin.SimpleListFilter):
    title = _('服务器环境')
    parameter_name = 'TransactionEconomyIndustryProductsProjectServerAdminMirrorCategory'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='ServerEnvironment').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(SERVER_ENVIRONMENT=self.value())


class TransactionEconomyIndustryProductsProductsServerAdminServerEnvironment(admin.SimpleListFilter):
    title = _('服务器环境')
    parameter_name = 'TransactionEconomyIndustryProductsProductsServerAdminServerEnvironment'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='ServerEnvironment').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(SERVER_ENVIRONMENT=self.value())


class TransactionEconomyIndustryProductsProductsProjectAdmin(admin.SimpleListFilter):
    title = _('项目产品关联')
    parameter_name = 'TransactionEconomyIndustryProductsProductsProjectAdmin'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='CorrelationProjectProducts').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(CORRELATION_CODE=self.value())


class ProvenanceSystemSettingsMenuManagementMenuParameterAdminType(admin.SimpleListFilter):
    title = _('菜单节点类型')
    parameter_name = 'ProvenanceSystemSettingsMenuManagementMenuParameterAdmin'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='MenuNodeType').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(NODE_TYPE=self.value())


class LearningTheHumanitiesHumanitiesArtsLiteratureArtContentTypeAdminType(admin.SimpleListFilter):
    title = _('菜单节点类型')
    parameter_name = 'LearningTheHumanitiesHumanitiesArtsLiteratureArtContentTypeAdminType'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='LiteratureArtContentCode').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(LITERATURE_ART_CODE=self.value())


class CommunalCallCode(admin.SimpleListFilter):
    title = _('称呼类型')
    parameter_name = 'LearningTheHumanitiesHumanitiesArtsLiteratureArtContentTypeAdminType'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='CallCode').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(NAME_CODE=self.value())


class LearningNaturalScienceBiologicalSpeciesCallCode(admin.SimpleListFilter):
    title = _('生物种类称呼')
    parameter_name = 'LearningNaturalScienceBiologicalSpeciesCallCode'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='CallCode').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(ENTERPRISE_NAME_CODE=self.value())


class ProvenanceSystemFunctionDataRecordsSystemAdminCode(admin.SimpleListFilter):
    title = _('所属系统')
    parameter_name = 'ProvenanceSystemFunctionDataRecordsSystemAdminCode'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='SystemCategory').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(SYSTEM_CATEGORY=self.value())


class ProvenanceSystemFunctionDataRecordsSystemFileObjectAdminType(admin.SimpleListFilter):
    title = _('对象类型')
    parameter_name = 'ProvenanceSystemFunctionDataRecordsSystemFileObjectAdminType'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='FileObjectCode').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(TYPE=self.value())


class ProvenanceSystemFunctionDataRecordsSystemFileObjectInheritType(admin.SimpleListFilter):
    title = _('文件对象继承配置')
    parameter_name = 'ProvenanceSystemFunctionDataRecordsSystemFileObjectInheritType'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='FileObjectInheritType').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(INHERIT_TYPE=self.value())


class ProvenanceSystemFunctionDevelopInformationSystemAdminSystemCategory(admin.SimpleListFilter):
    title = _('所属系统')
    parameter_name = 'ProvenanceSystemFunctionDevelopInformationSystemAdminSystemCategory'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='SystemCategory').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(SYSTEM_CATEGORY=self.value())


class ProvenanceSystemFunctionDevelopInformationSystemAdminSystemArchitecture(admin.SimpleListFilter):
    title = _('系统架构')
    parameter_name = 'ProvenanceSystemFunctionDevelopInformationSystemAdminSystemArchitecture'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='SystemArchitecture').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(ARCHITECTURE=self.value())
