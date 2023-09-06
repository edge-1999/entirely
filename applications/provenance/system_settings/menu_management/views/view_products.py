from work_records.result import RecordsOrganizations
from project.result import OrganizationProject
from products.result import ProjectProducts
from project_server.result import ProjectServer


class ViewProducts(object):
    def __init__(self, subscriber_id):
        self.subscriber_id = subscriber_id
        self.display = False
        self.data = []
        self.__def_get_()

    @property
    def dict(self):
        return self.__dict__

    def __def_get_(self):
        if self.subscriber_id:
            render_data = {}
            organizations = RecordsOrganizations(self.subscriber_id)
            if organizations.display:
                organizations_dict = []
                for organization in organizations.data:
                    organization.get('ID_ORGANIZATIONS')
                    organizations_dict.append({
                        "ID_ORGANIZATIONS": organization.get('ID_ORGANIZATIONS'),
                        "ORGANIZATIONS_NAME": organization.get('ORGANIZATIONS_NAME'),
                    })
                    projects = OrganizationProject(organization.get('ID_ORGANIZATIONS'))
            # OrganizationProject()
            # ProjectProducts()
            # ProjectServer()
            self.display = True
