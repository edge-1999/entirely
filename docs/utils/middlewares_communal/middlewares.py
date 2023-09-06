from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

from account_management.models import (
    ProvenanceSystemSettingsAccountManagementSubscriberGroupAccount,
    ProvenanceSystemSettingsAccountManagementRoleSubscriber,
    ProvenanceSystemSettingsAccountManagementRoleSubscriberGroup,
    ProvenanceSystemSettingsAccountManagementRole,
    ProvenanceSystemSettingsAccountManagementSubscriberGroup,
    ProvenanceSystemSettingsAccountManagementSubscriber
)
from menu_management.models import (
    ProvenanceSystemSettingsMenuManagementMenu,
    ProvenanceSystemSettingsMenuManagementMenuParameter,
    ProvenanceSystemSettingsMenuManagementMenuRoleDisplay
)


class PasswordChangeMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path == '/password_change/':
            return render(request, 'password_change.html')


class SubscriberRoleMenuNode(object):
    def __init__(self, menu_id, role_id):
        self.menu_id = menu_id  # 菜单ID
        self.role_id = role_id  # 菜单所有的角色 set()
        self.name = None  # 菜单的名字
        self.icon = None  # 菜单的图标
        self.node_type = None  # 菜单的图标
        self.url = None  # 菜单的url
        self.codename = None  # 菜单所有的角色 set()
        self.children = []  # 树的孩子结点
        self.parent = None  # 树的父结点
        self._def_get_menu_parameter()

    def _def_get_menu_parameter(self):
        menu_p = ProvenanceSystemSettingsMenuManagementMenu.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, id=self.menu_id,
        ).values('id', 'NAME').distinct().first()
        if menu_p:
            self.name = menu_p['NAME']
            parameter = ProvenanceSystemSettingsMenuManagementMenuParameter.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, id=menu_p['id']
            ).values('ICON', 'APP_URL_NAME', 'URL_NAME', 'NODE_TYPE__ABBREVIATION').distinct().first()
            if parameter:
                self.icon = parameter.get('ICON')
                self.node_type = parameter.get('NODE_TYPE__ABBREVIATION')
                # self.url = parameter.get('APP_URL_NAME') + ':' + parameter.get('URL_NAME')

    def add_child(self, child):
        child.parent = self  # 要添加的父结点是self
        self.children.append(child.dict)  # 父结点self的children添加child
        return True

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
        if self.icon:
            data.update(
                {
                    "icon": self.icon,
                }
            )
        if self.url:
            data.update(
                {
                    "url": self.url,
                }
            )
        if self.node_type:
            data.update(
                {
                    "node": self.node_type,
                }
            )
        return data


class SubscriberExist(object):
    """判断用户是否存在"""

    def __init__(self, subscriber_id):
        self.subscriber_id = None if not ProvenanceSystemSettingsAccountManagementSubscriber.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID=subscriber_id
        ).exists() else subscriber_id


class SubscriberRoleMenu(SubscriberExist):
    """
    返回展示的菜单
    """

    def __init__(self, subscriber_id=None):
        super().__init__(subscriber_id)
        self.role_id = set()
        self.role_default_id = 18
        self.group_id = None
        self._subscriber_group = set()  # 用户组：用户所属的用户组
        self._subscriber_group_son = set()  # 用户组_下级：根据用户所属用户组，找到所有下级用户组
        self._role_subscriber = set()  # 用户_角色：用户拥有的角色
        self._role_son_subscriber = set()  # 用户_角色_下级：根据用户拥有的角色找到的下级角色
        self._role_subscriber_group = set()  # 用户组_角色：用户组拥有的角色
        self._role_son_subscriber_group = set()  # 用户组-角色-下级角色：用户组拥有的下级角色
        self._role_subscriber_group_son = set()  # 用户组_下级用户组_角色：所有的下级用户组，找到对应的角色
        self._role_son_subscriber_group_son = set()  # 用户组_下级用户组_角色_下级角色：所有的下级用户组角色的下级角色
        self.menu_tree = []
        if self.subscriber_id:
            self._def_subscriber()
        else:
            self.role_id.add(self.role_default_id)
            # self.role_id.update()

    @property
    def dict(self):
        data = {
            'subscriber': self.subscriber_id,
            'group': list(self.group_id if self.group_id else []),
            'role': list(self.role_id if self.role_id else []),
        }
        if self.menu_tree:
            data.update({"menu_tree": list(self.menu_tree)})
        return data

    def _def_subscriber(self):
        """用户角色"""
        self._def_subscriber_role()
        if self._role_subscriber:
            for r_id in self._role_subscriber:
                self._def_subscriber_role_son(r_id)
        self._def_subscriber_group()
        if self._subscriber_group:
            self._def_subscriber_group_role()
            if self._role_subscriber_group:
                for g_id in self._role_subscriber_group:
                    self._def_subscriber_group_role_son(g_id)
            for g_i in self._subscriber_group:
                self._def_subscriber_group_son(g_i)
                if self._subscriber_group_son:
                    self._def_subscriber_group_son_role()
                    if self._role_subscriber_group_son:
                        for i in self._role_subscriber_group_son:
                            self._def_subscriber_group_son_role_son(i)
        self.group_id = set.union(self._subscriber_group, self._subscriber_group_son)
        self.role_id = set.union(
            self._role_subscriber, self._role_son_subscriber, self._role_subscriber_group,
            self._role_son_subscriber_group, self._role_subscriber_group_son, self._role_son_subscriber_group_son,
        )

    def _def_subscriber_role(self):
        """
        用户的角色
        :return:
        :rtype:
        """
        role_s = ProvenanceSystemSettingsAccountManagementRoleSubscriber.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_SUBSCRIBER__ID=self.subscriber_id
        ).values('ID_ROLE')
        if role_s.exists():
            for role_id in role_s:
                self._role_subscriber.add(role_id["ID_ROLE"])

    def _def_subscriber_role_son(self, p_id):
        """
        当前所属用户角色的所有下级角色
        :return:
        :rtype:
        """
        group_id = ProvenanceSystemSettingsAccountManagementRole.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=p_id
        ).values('id')
        if group_id.exists():
            for g_id in group_id:
                self._def_subscriber_role_son(g_id['id'])
                self._role_son_subscriber.add(g_id['id'])

    def _def_subscriber_group(self):
        """
        用户所属的用户组
        :return:
        :rtype:
        """
        s_g = ProvenanceSystemSettingsAccountManagementSubscriberGroupAccount.objects.filter(
            STATUS_IS_DELETE='0', ID_SUBSCRIBER=self.subscriber_id, STATUS_IS_EFFECTIVE=1).values(
            'ID_SUBSCRIBER_GROUP')
        if s_g.exists():
            for son_id in s_g:
                self._subscriber_group.add(son_id["ID_SUBSCRIBER_GROUP"])

    def _def_subscriber_group_role(self):
        """
        用户组拥有的角色
        :return:
        :rtype:
        """
        for g_id in self._subscriber_group:
            r_id = ProvenanceSystemSettingsAccountManagementRoleSubscriberGroup.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_SUBSCRIBER_GROUP=g_id
            ).values('ID_ROLE')
            if r_id.exists():
                for subscriber_group_id in r_id:
                    self._role_subscriber_group.add(subscriber_group_id["ID_ROLE"])

    def _def_subscriber_group_role_son(self, p_id):
        """
        根据用户组拥有的角色，寻找到所有子集角色
        :return:
        :rtype:
        """
        role_id = ProvenanceSystemSettingsAccountManagementRole.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=p_id).values('id', 'NAME', 'ID_PARENT')
        if role_id.exists():
            for r_id in role_id:
                self._def_subscriber_group_role_son(r_id['id'])
                self._role_son_subscriber_group.add(r_id['id'])

    def _def_subscriber_group_son(self, p_id):
        """
        当前所属用户组的所有下级用户组
        :return:
        :rtype:
        """
        group_id = ProvenanceSystemSettingsAccountManagementSubscriberGroup.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=p_id
        ).values('id')
        if group_id.exists():
            for g_id in group_id:
                self._def_subscriber_group_son(g_id['id'])
                self._subscriber_group_son.add(g_id['id'])

    def _def_subscriber_group_son_role(self):
        """
        下级用户组拥有的角色
        :return:
        :rtype:
        """
        g_id_son = ProvenanceSystemSettingsAccountManagementRoleSubscriberGroup.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_SUBSCRIBER_GROUP_id__in=self._subscriber_group_son,

        ).values('ID_ROLE')
        if g_id_son.exists():
            for g_id in g_id_son:
                self._role_subscriber_group_son.add(g_id["ID_ROLE"])

    def _def_subscriber_group_son_role_son(self, p_id):
        """
        下级用户组角色的下级角色
        :return:
        :rtype:
        """
        son_id = ProvenanceSystemSettingsAccountManagementRole.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=p_id
        ).values('id')
        if son_id.exists():
            for s_id in son_id:
                self._def_subscriber_group_son_role_son(s_id["id"])
                self._role_son_subscriber_group_son.add(s_id["id"])

    def __def_menu_recursion(self, p_id=None, node=None):
        menu_son = ProvenanceSystemSettingsMenuManagementMenu.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=p_id
        ).exclude(
            provenancesystemsettingsmenumanagementmenuroledisplay__ID=None,
            provenancesystemsettingsmenumanagementmenuroledisplay__STATUS_IS_DELETE=1,
            provenancesystemsettingsmenumanagementmenuroledisplay__STATUS_IS_EFFECTIVE=0,
        ).values('id').distinct()
        if menu_son.exists():
            for menu_id in menu_son:
                menu_role_id = ProvenanceSystemSettingsMenuManagementMenu.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=p_id, id=menu_id["id"],
                    provenancesystemsettingsmenumanagementmenuroledisplay__STATUS_IS_DELETE='0',
                    provenancesystemsettingsmenumanagementmenuroledisplay__STATUS_IS_EFFECTIVE=1,
                ).exclude(
                    provenancesystemsettingsmenumanagementmenuroledisplay__ID=None,
                    provenancesystemsettingsmenumanagementmenuroledisplay__STATUS_IS_DELETE=1,
                    provenancesystemsettingsmenumanagementmenuroledisplay__STATUS_IS_EFFECTIVE=0,
                ).values('provenancesystemsettingsmenumanagementmenuroledisplay__ID_ROLE').distinct()
                if menu_role_id.exists():
                    distinct_role = set()
                    for role_id in menu_role_id:
                        distinct_role.add(role_id["provenancesystemsettingsmenumanagementmenuroledisplay__ID_ROLE"])
                    if self.role_id & distinct_role:
                        menu_mode = SubscriberRoleMenuNode(menu_id["id"], distinct_role)
                        if node:
                            node.add_child(menu_mode)
                        else:
                            self.menu_tree.append(menu_mode.dict)
                        self.__def_menu_recursion(menu_id["id"], menu_mode)

    def def_menu_default(self):
        """默认菜单"""
        menu_list = ProvenanceSystemSettingsMenuManagementMenu.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=10,
            provenancesystemsettingsmenumanagementmenuroledisplay__ID_ROLE=self.role_default_id
        ).exclude(
            provenancesystemsettingsmenumanagementmenuroledisplay__ID=None,
            provenancesystemsettingsmenumanagementmenuroledisplay__STATUS_IS_DELETE=1,
            provenancesystemsettingsmenumanagementmenuroledisplay__STATUS_IS_EFFECTIVE=0,
        ).values('id', 'NAME', 'ID_PARENT').distinct()
        if menu_list.exists():
            return_menu_list = []
            for menu_id in menu_list:
                parameter = ProvenanceSystemSettingsMenuManagementMenuParameter.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_MENU=menu_id.get('id')
                ).values(
                    'APP_URL_NAME', 'URL_NAME', 'ICON', 'NODE_TYPE',
                    'NODE_TYPE__TECHNOLOGY')
                if parameter.exists():
                    menu_parameter = {
                        "ID": menu_id.get('id'),
                        "APP_URL_NAME": parameter.first().get('APP_URL_NAME'),
                        "URL_NAME": parameter.first().get('URL_NAME'),
                        "ICON": parameter.first().get('ICON'),
                        "NODE_TYPE": parameter.first().get('NODE_TYPE__TECHNOLOGY'),
                    }
                    return_menu_list.append(menu_parameter)
            return return_menu_list

    def def_menu_display(self, menu_id):
        """
        判断传入的菜单有无查看权限
        :return:
        :rtype:
        """
        return ProvenanceSystemSettingsMenuManagementMenuRoleDisplay.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_MENU=menu_id, ID_ROLE__in=list(self.role_id),
            ID_ROLE__STATUS_IS_DELETE='0', ID_ROLE__STATUS_IS_EFFECTIVE=1
        ).exists()

    @property
    def run(self):
        import json
        self.__def_menu_recursion()
        return json.dumps(self.dict, ensure_ascii=False)


class SubscriberRoleMenuMiddleware(MiddlewareMixin):
    """
    根据传入的菜单标识，返回展示的菜单（权限控制）
    """

    def process_request(self, request):
        """钩子方法"""
        # 1.判断是否登陆 无论登陆不登陆 都需要SubscriberRoleMenu() 登陆传入标识
        # SubscriberRoleMenu()
        pass

    def process_view(self, request, callback, callback_args, callback_kwargs):
        """检查权限"""
        # 2.判断是否有菜单的权限，再做标识 返回数据。
        # 3.没有权限做特殊处理，查看是否登陆，是否异常请求、需要屏蔽IP、永久性的，壮大黑名单ID，并且编写征信黑名单相关信息。
        # 4.删除 实例化的 SubscriberRoleMenu() 参数
        pass
