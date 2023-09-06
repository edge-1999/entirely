from project.models import TransactionEconomyIndustryProductsProjectBasis


class OrganizationProject(object):
    def __init__(self, organization_id):
        """属于组织的项目"""
        self.organization_id = organization_id
        self.display = False
        self.data = []
        self.__def_project_message()

    @property
    def dict(self):
        return self.__dict__

    def __def_project_message(self):
        """获取项目所属的组织"""
        if self.organization_id:
            data_projects = TransactionEconomyIndustryProductsProjectBasis.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1,
                transactioneconomyindustryproductsprojectorganization__ID_ORGANIZATIONS=self.organization_id,
                transactioneconomyindustryproductsprojectorganization__STATUS_IS_DELETE=0,
                transactioneconomyindustryproductsprojectorganization__STATUS_IS_EFFECTIVE=1,
            ).values(
                'ID', 'PROJECT_NAME', 'PROJECT_CREATION_TIME', 'PROJECT_END_TIME', 'DETAIL',
                'transactioneconomyindustryproductsprojectorganization__PROPORTION'
            ).distinct()
            if data_projects.exists():
                for project_data in data_projects:
                    return_data = {
                        "ID_PROJECT": project_data.get("ID").hex,
                        "PROJECT_NAME": project_data.get("PROJECT_NAME"),
                        "PROJECT_CREATION_TIME": project_data.get("PROJECT_CREATION_TIME"),
                        "PROJECT_END_TIME": project_data.get("PROJECT_END_TIME"),
                        "PROJECT_DETAIL": project_data.get("DETAIL"),
                        "PROPORTION": project_data.get(
                            "transactioneconomyindustryproductsprojectorganization__PROPORTION"),
                    }
                    self.display = True
                    self.data.append(return_data)
