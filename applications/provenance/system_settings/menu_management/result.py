from django.shortcuts import reverse

from menu_management.models import (
    ProvenanceSystemSettingsMenuManagementMenuRoleDisplay,
    ProvenanceSystemSettingsMenuManagementMenuParameter,
    ProvenanceSystemSettingsMenuManagementMenu,
)
from routing_management.result import RoutingManagement


class MenuNode(object):
    def __init__(self, menu_id):
        self.name = None  # 菜单的名字
        self.menu_id = menu_id  # 菜单ID
        self.parent_id = None  # 父菜单ID
        self.url = None  # 菜单的url
        self.icon = None  # 菜单的图标
        self.node_type = None  # 菜单的图标
        self.role_id = []  # 菜单所有的角色 set()
        self.authority_id = None  # 菜单所有权限
        self.children = []  # 树的孩子结点
        self.parent = None  # 树的父结点
        self._def_get_menu_parameter()

    @property
    def dict(self):
        data = {
            "menu": self.menu_id,
            # "role": list(self.role_id),
            "children": self.children,
        }
        if self.name:
            data.update(
                {
                    "name": self.name,
                }
            )
        # if self.icon:
        #     data.update(
        #         {
        #             "icon": self.icon,
        #         }
        #     )
        # if self.url:
        #     data.update(
        #         {
        #             "url": self.url,
        #         }
        #     )
        if self.node_type:
            data.update(
                {
                    "node": self.node_type,
                }
            )
        # if self.children:
        #     data.update({
        #         "children": self.children,
        #     })
        return data

    def _def_get_menu_parameter(self):
        menu_p = ProvenanceSystemSettingsMenuManagementMenu.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, id=self.menu_id,
        ).values('id', 'NAME', "ID_PARENT").distinct()
        if menu_p.exists():
            menu_p = menu_p.first()
            self.name = menu_p.get('NAME')
            self.parent_id = menu_p.get('ID_PARENT')
            parameter = ProvenanceSystemSettingsMenuManagementMenuParameter.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_MENU=menu_p['id']
            ).values('ICON', "NAME_SPACE", 'NODE_TYPE__ABBREVIATION').distinct()
            if parameter.exists():
                parameter = parameter.first()
                self.icon = parameter.get('ICON')
                self.node_type = parameter.get('NODE_TYPE__ABBREVIATION')
                routing_url_id = parameter.get('NAME_SPACE')
                if routing_url_id:
                    routing_management = RoutingManagement()
                    routing_management.get_routing_management(routing_url_id)
                    if routing_management.data:
                        self.url = routing_management.data[0].get(routing_url_id)
            menus_roles = ProvenanceSystemSettingsMenuManagementMenuRoleDisplay.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_MENU=menu_p['id']
            ).values('ID_ROLE').distinct()
            if menus_roles.exists():
                for menu_role in menus_roles:
                    self.role_id.append(menu_role.get('ID_ROLE'))
                self.role_id = list(set(self.role_id))

    def add_child(self, child):
        child.parent = self  # 要添加的父结点是self
        self.children.append(child.dict)  # 父结点self的children添加child
        return True

    @property
    def dict_all(self):
        data = {
            "menu_id": self.menu_id,
            "menu_name": self.name,
            "menu_parent_id": self.parent_id,
            "menu_url": self.url,
            "menu_icon": self.icon,
            "menu_node_type": self.node_type,
            "menu_role": self.role_id,
            "menu_authority": self.authority_id,
            "menu_children": self.children,
        }
        return data

    def add_all_child(self, child):
        child.parent = self  # 要添加的父结点是self
        self.children.append(child.dict_all)  # 父结点self的children添加child

    @property
    def dict_effective(self):
        data = {
            "menu_id": self.menu_id,
            "menu_children": self.children,
        }
        if self.name:
            data.update({
                "menu_name": self.name,
            })
        if self.parent_id:
            data.update({
                "menu_parent_id": self.parent_id,
            })
        if self.url:
            data.update({
                "menu_url": self.url,
            })
        if self.icon:
            data.update({
                "menu_icon": self.icon,
            })
        if self.node_type:
            data.update({
                "menu_node_type": self.node_type,
            })
        if self.role_id:
            data.update({
                "menu_role": self.role_id,
            })
        if self.authority_id:
            data.update({
                "menu_authority": self.authority_id,
            })
        # if self.children:
        #     data.update({
        #         "menu_children": self.children,
        #     })
        return data

    def add_effective_child(self, child):
        child.parent = self  # 要添加的父结点是self
        self.children.append(child.dict_effective)  # 父结点self的children添加child


class MenusManagement(object):
    """获取所有菜单的信息"""

    def __init__(self):
        self.role_id = set()
        self.role_default_id = 18
        self.role_id.add(self.role_default_id)
        self.group_id = None
        self.menu_tree = []

    def def_run_menu_level_show(self, parent_id=None, node=None):
        """展示所有目录层级"""
        menu_tree = []
        menus_son = ProvenanceSystemSettingsMenuManagementMenu.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=parent_id
        ).values('id').distinct()
        if menus_son.exists():
            for menu_son in menus_son:
                menu_mode = MenuNode(menu_son.get("id"))
                if node:
                    node.add_child(menu_mode)
                else:
                    menu_tree.append(menu_mode.dict)
                self.def_run_menu_level_show(menu_son["id"], menu_mode)
        return menu_tree

    def def_run_menu_level_show_all(self, parent_id=None, node=None):
        """展示菜单的所有信息"""
        menu_tree = []
        menus_son = ProvenanceSystemSettingsMenuManagementMenu.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=parent_id
        ).values('id').distinct()
        if menus_son.exists():
            for menu_son in menus_son:
                menu_mode = MenuNode(menu_son.get("id"))
                if node:
                    node.add_all_child(menu_mode)
                else:
                    menu_tree.append(menu_mode.dict_all)
                self.def_run_menu_level_show_all(menu_son["id"], menu_mode)
        return menu_tree

    def def_run_menu_level_show_effective(self, parent_id=None, node=None):
        """展示菜单的所有有效信息"""
        menu_tree = []
        menus_son = ProvenanceSystemSettingsMenuManagementMenu.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=parent_id
        ).values('id').distinct()
        if menus_son.exists():
            for menu_son in menus_son:
                menu_mode = MenuNode(menu_son.get("id"))
                if node:
                    node.add_effective_child(menu_mode)
                else:
                    menu_tree.append(menu_mode.dict_effective)
                self.def_run_menu_level_show_all(menu_son["id"], menu_mode)
        return menu_tree


class MenuManagement(object):
    """菜单相关信息"""

    def __init__(self, menu_id, role_list):
        """当前菜单操作"""
        self.menu_id = menu_id
        self.role_list = role_list
        self.display = False
        self.data = []

    def def_determine_menu_role(self, menu_id) -> bool:
        """判断菜单权限"""
        son_role_menus = ProvenanceSystemSettingsMenuManagementMenuRoleDisplay.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_MENU=menu_id,
        ).values("ID_ROLE").distinct()
        if son_role_menus.exists():
            if {str(son_role_menu.get('ID_ROLE')) for son_role_menu in son_role_menus} & set(self.role_list):
                return True
        return False


class MenuSonManagement(MenuManagement):
    """获取子菜单信息"""

    def __init__(self, menu_id, role_list):
        super().__init__(menu_id, role_list)

    def def_run_son_menu_message(self):
        """获取当前子菜单信息"""
        return_data_list = []
        self.display = False
        if self.menu_id:
            son_menus_data = ProvenanceSystemSettingsMenuManagementMenuRoleDisplay.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_MENU__ID_PARENT=self.menu_id,
                ID_MENU__STATUS_IS_DELETE='0', ID_MENU__STATUS_IS_EFFECTIVE=1,
                ID_MENU__provenancesystemsettingsmenumanagementmenuparameter__STATUS_IS_DELETE='0',
                ID_MENU__provenancesystemsettingsmenumanagementmenuparameter__STATUS_IS_EFFECTIVE=1,
            ).values("ID_MENU").distinct()
            if son_menus_data.exists():
                son_menu_set = {str(son_menu.get('ID_MENU')) for son_menu in son_menus_data}
                for menu_id in son_menu_set:
                    if self.def_determine_menu_role(menu_id):
                        if self.__def_while_get_menu_tree_type(menu_id, False):
                            son_menu_data = self.__def_get_son_menu_message(menu_id)
                            if son_menu_data:
                                self.display = True
                                return_data_list.append(son_menu_data)
        return return_data_list

    def __def_while_get_menu_tree_type(self, menu_id, mark):
        """递归获取菜单的数据节点，并判断是否存在数据节点，如果有数据节点则返回True"""
        __mark = mark
        menus_data = ProvenanceSystemSettingsMenuManagementMenuRoleDisplay.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_MENU__ID_PARENT=menu_id,
            ID_MENU__STATUS_IS_DELETE='0', ID_MENU__STATUS_IS_EFFECTIVE=1,
            ID_MENU__provenancesystemsettingsmenumanagementmenuparameter__STATUS_IS_DELETE='0',
            ID_MENU__provenancesystemsettingsmenumanagementmenuparameter__STATUS_IS_EFFECTIVE=1,
        ).values(
            "ID_ROLE", "ID_MENU",
            'ID_MENU__provenancesystemsettingsmenumanagementmenuparameter__NODE_TYPE__TECHNOLOGY').distinct()
        if menus_data.exists():
            for menu_data in menus_data:
                menu_node_id = menu_data.get("ID_MENU")
                menu_role_id = menu_data.get("ID_ROLE")
                menu_node_type = menu_data.get(
                    "ID_MENU__provenancesystemsettingsmenumanagementmenuparameter__NODE_TYPE__TECHNOLOGY")
                if str(menu_role_id) in self.role_list:
                    if menu_node_type == "datanode":
                        # if str(menu_role_id) in self.role_list:
                        __mark = True
                        return True
                    elif menu_node_type == "scope":
                        __mark = self.__def_while_get_menu_tree_type(menu_node_id, __mark)
                    elif menu_node_type in ["scope", "module", "rule", "derive", "beginning", "fuzzy", "folder"]:
                        __mark = self.__def_while_get_menu_tree_type(menu_node_id, __mark)
        return __mark

    def __def_get_son_menu_message(self, son_menu_id):
        """获取传入菜单的信息，判断参数是都为数据节节点，目录节点，返回能看到的菜单"""
        son_menu_data = ProvenanceSystemSettingsMenuManagementMenuParameter.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_MENU=son_menu_id,
        ).values(
            "ID_MENU", "NAME_SPACE", "ICON", "NODE_TYPE__TECHNOLOGY", "NODE_TYPE__ABBREVIATION",
            "ID_MENU__NAME").distinct()
        if son_menu_data.exists():
            son_menu = son_menu_data.first()
            routing_url_id = son_menu.get("NAME_SPACE")
            if routing_url_id:
                routing_url_id = routing_url_id.hex
                routing_management = RoutingManagement()
                routing_management.get_routing_management(routing_url_id)
                if routing_management.data:
                    return {
                        "ID_MENU": son_menu.get("ID_MENU"),
                        "MENU_NAME": son_menu.get("ID_MENU__NAME"),
                        "MENU_TYPE": son_menu.get("NODE_TYPE__TECHNOLOGY"),
                        "MENU_ICON": son_menu.get("ICON"),
                        "MENU_URL": routing_management.data[0].get(routing_url_id),
                    }
