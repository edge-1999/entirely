from work_records.models import ProvenanceSystemFunctionWorkRecordsOrganizations


class RecordsOrganizations(object):
    """通过账户找到所属组织"""

    def __init__(self, subscriber_id):
        self.subscriber_id = subscriber_id
        self.display = False
        self.data = []
        self.__def_get_organizations()

    def __def_get_organizations(self):
        data_organizations = ProvenanceSystemFunctionWorkRecordsOrganizations.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_SUBSCRIBER=self.subscriber_id,
            ID_ORGANIZATIONS__STATUS_IS_DELETE='0', ID_ORGANIZATIONS__STATUS_IS_EFFECTIVE=1,
        ).values('ID_ORGANIZATIONS', "ID_ORGANIZATIONS__ENTERPRISE_NAME")
        if data_organizations.exists():
            for organization in data_organizations:
                return_data = {
                    "ID_ORGANIZATIONS": organization.get('ID_ORGANIZATIONS').hex,
                    "ORGANIZATIONS_NAME": organization.get('ID_ORGANIZATIONS__ENTERPRISE_NAME'),
                }
                self.data.append(return_data)
                self.display = True

    @property
    def dict(self):
        return self.__dict__
