from django.shortcuts import reverse

from routing_management.models import ProvenanceSystemSettingsRoutingManagementNameSpaceName


class RoutingManagement(object):
    """获取路由的信息"""

    def __init__(self, routing_id=None):
        self.routing_id = routing_id
        self.display = False
        self.data = []

    def get_routing_all_management(self):
        """获取所有的路由"""
        self.data.clear()
        self.display = False
        routing_data = ProvenanceSystemSettingsRoutingManagementNameSpaceName.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1,
        ).values("ID", "ID_NAME_SPACE__NAME_SPACE", "ID_NAME_SPACE__NAME", "NAME_SPACE_NAME", "NAME").distinct()
        if routing_data.exists():
            routing_data = routing_data.first()
            routing_url = reverse(
                routing_data.get("ID_NAME_SPACE__NAME_SPACE") + ':' + routing_data.get("NAME_SPACE_NAME"))
            routing_name = routing_data.get("ID_NAME_SPACE__NAME") + ':' + routing_data.get("NAME")
            return_data = {
                "routing_id": routing_data.get('ID'),
                "routing_url": routing_url,
                "routing_name": routing_name,
            }
            self.data.append(return_data)
            self.display = True
        return self.data

    def get_routing_management(self, routing_id):
        """获取指定路由信息"""
        self.data.clear()
        self.display = False
        routing_data = ProvenanceSystemSettingsRoutingManagementNameSpaceName.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID=routing_id,
        ).values("ID", "ID_NAME_SPACE__NAME_SPACE", "NAME_SPACE_NAME").distinct()
        if routing_data.exists():
            routing_data = routing_data.first()
            routing_url = reverse(
                routing_data.get("ID_NAME_SPACE__NAME_SPACE") + ':' + routing_data.get("NAME_SPACE_NAME"))
            return_data = {
                routing_id: routing_url,
            }
            self.data.append(return_data)
            self.display = True
        return self.data
