from develop_information.models import ProvenanceSystemFunctionDevelopInformationSystem


class DevelopInformationNode(object):
    def __init__(self, system_id):
        self.id_system = system_id  # 系统标识
        self.display = True if self.id_system else False  # 标记
        self.system_name = None  # 系统名称
        self.id_system_person = None  # 所属人员
        self.system_port = None  # IP
        self.system_category = None  # 所属系统
        self.system_organization = None  # 所属组织
        self.system_machine = None  # 虚拟机
        self.id_parent_system = None  # 上级系统
        self.system_architecture = None  # 系统架构
        self.system_product = None  # 依赖产品

    def def_get_system_message(self):
        system_data = ProvenanceSystemFunctionDevelopInformationSystem.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID=self.id_system,
        ).values(
            'ID_PERSON', 'NAME', 'IP', 'SYSTEM_CATEGORY__ABBREVIATION', 'ID_ORGANIZATIONS', 'IS_VIRTUAL_MACHINE',
            'ID_SYSTEM', 'ARCHITECTURE__ABBREVIATION', 'ID_PRODUCTS')
        if system_data.exists():
            system_data = system_data.first()
            self.system_name = system_data.get('NAME')
            self.id_system_person = system_data.get('ID_PERSON').hex if system_data.get('ID_PERSON') else ''
            self.system_port = system_data.get('IP')
            self.system_category = system_data.get('SYSTEM_CATEGORY__ABBREVIATION')
            self.system_organization = system_data.get('ID_ORGANIZATIONS').hex \
                if system_data.get('ID_ORGANIZATIONS') else ''
            self.system_machine = 'X' if system_data.get('system_machine') else ''
            self.id_parent_system = system_data.get('ID_SYSTEM').hex if system_data.get('ID_SYSTEM') else ''
            self.system_architecture = system_data.get('ARCHITECTURE__ABBREVIATION') \
                if system_data.get('ARCHITECTURE__ABBREVIATION') else ''
            self.system_product = system_data.get('ID_PRODUCTS').hex if system_data.get('ID_PRODUCTS') else ''
