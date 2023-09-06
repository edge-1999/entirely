from project_server.models import TransactionEconomyIndustryProductsProjectServer


class ProjectServer(object):
    def __init__(self, server_id):
        """服务器信息"""
        self.server_id = server_id
        self.display = False
        self.data = []
        self.__def_server_message()

    @property
    def dict(self):
        return self.__dict__

    def __def_server_message(self):
        """获取项目所属的组织"""
        if self.server_id:
            data_servers = TransactionEconomyIndustryProductsProjectServer.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID=self.server_id,
            ).values(
                'ID', 'NAME', "INSTANCE_ID", "PUBLIC_NETWORK", "REGION", "SYSTEM_CATEGORY",
                "MIRROR_CATEGORY", "INSIDE_OUTSIDE_CODE__ABBREVIATION",
            ).distinct()
            if data_servers.exists():
                for data_server in data_servers:
                    return_data = {
                        "ID_SERVER": data_server.get("ID").hex,
                        "SERVER_NAME": data_server.get("NAME"),
                        "SERVER_INSTANCE_ID": data_server.get("INSTANCE_ID"),
                        "SERVER_PUBLIC_NETWORK": data_server.get("PUBLIC_NETWORK"),
                        "SERVER_REGION": data_server.get("REGION"),
                        "SERVER_SYSTEM": data_server.get("SYSTEM_CATEGORY"),
                        "SERVER_MIRROR": data_server.get("MIRROR_CATEGORY"),
                        "SERVER_INTERNET": data_server.get("INSIDE_OUTSIDE_CODE__ABBREVIATION"),
                    }
                    self.data.append(return_data)
                    self.display = True
