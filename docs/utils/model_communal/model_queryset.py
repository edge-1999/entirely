from standard_encoding.models import ProvenanceSystemSettingsStandardCodeMainDict


def get_queryset_function_authority_type_data():
    """权限控制-数据"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='PermissionControlData')


def get_queryset_function_permission_control_menu():
    """权限控制-操作"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='PermissionControlMenu')


def get_queryset_function_person_sex_physiological():
    """人类生理性别"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='HumanPhysiologicalGender')


def get_queryset_function_calendar():
    """日历"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='Calendar')


def get_queryset_function_personal_address():
    """个人地址"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='PersonalAddress')


def get_queryset_function_personal_event():
    """人员事件"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='PersonalEvent')


def get_queryset_function_organization_category():
    """组织类别"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='OrganizationCategory')


def get_queryset_function_organization_category_code():
    """组织称呼类型"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='OrganizationCategoryCode')


def get_queryset_function_organization_address_code():
    """组织地址类型"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='OrganizationAddressCode')


def get_queryset_function_organization_certificate_code():
    """组织证件类别"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='OrganizationsCertificateCode')


def get_queryset_function_person_certificate_code():
    """个人证件类别"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='PersonCertificateCode')


def get_queryset_function_products_type():
    """产品类型"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='ProductsType')


def get_queryset_records_event_type():
    """事件类型"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='RecordsEventType')


def get_queryset_records_event_identity():
    """事件参与身份"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='RecordsEventIdentity')


def get_queryset_password_correlation_code():
    """产品关联类别"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='PasswordCorrelationCode')


def get_queryset_politics_district_code():
    """城镇位置类别"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='PoliticsDistrictCode')


def get_queryset_account_management_subscriber_land():
    """关联登陆"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='SubscriberLandCode')


def get_queryset_function_products_project_server():
    """系统类别"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='SystemCategory')


def get_queryset_function_products_project_server_mirror_category():
    """镜像类别"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='MirrorCategory')


def get_queryset_function_products_project_server_internet_category():
    """互联网类别"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='InternetCategory')


def get_queryset_function_products_server_environment():
    """服务器环境"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='ServerEnvironment')


def get_queryset_function_products_products_project_correlation():
    """项目产品关联"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='CorrelationProjectProducts')


def get_queryset_system_menu_node_type():
    """菜单节点类型"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='MenuNodeType')


def get_queryset_literature_art_content_type():
    """文字艺术类别"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='LiteratureArtContentCode')


def get_queryset_function_call_code():
    """称呼类型"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='CallCode')


def get_queryset_project_server_code():
    """系统类别"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='SystemCategory')


def get_queryset_project_system_architecture():
    """系统架构"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='SystemArchitecture')


def get_queryset_file_object_code():
    """文件对象类型"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='FileObjectCode')


def get_queryset_file_object_inherit_code():
    """文件对象继承类型"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='FileObjectInheritType')
