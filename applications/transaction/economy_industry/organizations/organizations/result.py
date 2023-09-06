from organizations.models import TransactionEconomyIndustryOrganizationsBases, \
    TransactionEconomyIndustryOrganizationsCall, TransactionEconomyIndustryOrganizationsAddress, \
    TransactionEconomyIndustryOrganizationsCertificate, TransactionEconomyIndustryOrganizationsContact, \
    TransactionEconomyIndustryOrganizationsDetails


class OrganizationsMessage(object):
    """获取组织信息"""

    def __init__(self, organizations_id=None):
        self.organizations_id = organizations_id
        self.display = False
        self.data = []
        self.def_get_organization_message()

    def def_get_organization_message(self):
        """获取单个组织信息"""
        self.display = False
        if self.organizations_id:
            organization_data = TransactionEconomyIndustryOrganizationsBases.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID=self.organizations_id,
            ).values('ENTERPRISE_NAME', 'ENTERPRISE_CODE__ABBREVIATION', "COUNTRY_CREATE_TIME", "COUNTRY_END_TIME")
            if organization_data.exists():
                organization_data = organization_data.first()
                calls = TransactionEconomyIndustryOrganizationsCall.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_ORGANIZATIONS=self.organizations_id,
                ).values('ENTERPRISE_NAME_CODE__ABBREVIATION', 'ENTERPRISE_NAME', )
                address = TransactionEconomyIndustryOrganizationsAddress.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_ORGANIZATIONS=self.organizations_id,
                ).values('ENTERPRISE_ADDRESS_CODE__ABBREVIATION', 'ENTERPRISE_ADDRESS_NAME', )
                details = TransactionEconomyIndustryOrganizationsDetails.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_ORGANIZATIONS=self.organizations_id,
                ).values('DETAIL', )
                certificates = TransactionEconomyIndustryOrganizationsCertificate.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_ORGANIZATIONS=self.organizations_id,
                ).values(
                    'SIGNING_AND_ISSUING_ORGANIZATION', "SIGNING_AND_ISSUING_ORGANIZATION__ENTERPRISE_NAME",
                    'DATE_ISSUED', "CODE__ABBREVIATION", "NUMBER", "DATE_START", "DATE_END",
                )
                contacts = TransactionEconomyIndustryOrganizationsContact.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_ORGANIZATIONS=self.organizations_id,
                ).values('ID_PRODUCTS', 'ID_PRODUCTS__PRODUCTS_NAME', "NUMBER", )
                return_data = {
                    "ID_ORGANIZATION": self.organizations_id,
                    "ORGANIZATION_NAME": organization_data.get('ENTERPRISE_NAME'),
                    "ORGANIZATION_URL": organization_data.get('ENTERPRISE_CODE__ABBREVIATION'),
                    "ORGANIZATION_CREATE_TIME": organization_data.get('COUNTRY_CREATE_TIME'),
                    "ORGANIZATION_END_TIME": organization_data.get('COUNTRY_END_TIME'),
                    "ORGANIZATION_CALLS": [{
                        "CALL_NAME": call.get("ENTERPRISE_NAME"),
                        "CALL_NAME_CODE": call.get("ENTERPRISE_NAME_CODE__ABBREVIATION"),
                    } for call in calls] if calls.exists() else [],
                    "ORGANIZATION_ADDRESS": [{
                        "ADDR_NAME": addr.get("ENTERPRISE_ADDRESS_NAME"),
                        "ADDR_NAME_CODE": addr.get("ENTERPRISE_ADDRESS_CODE__ABBREVIATION"),
                    } for addr in address] if address.exists() else [],
                    "ORGANIZATION_CERTIFICATES": [{
                        "CERTIFICATE_ISSUING": certificate.get("SIGNING_AND_ISSUING_ORGANIZATION"),
                        "CERTIFICATE_ISSUING_NAME": certificate.get(
                            "SIGNING_AND_ISSUING_ORGANIZATION__ENTERPRISE_NAME"),
                        "CERTIFICATE_ISSUED_DATA": certificate.get("DATE_ISSUED"),
                        "CERTIFICATE_CODE": certificate.get("CODE__ABBREVIATION"),
                        "CERTIFICATE_NUMBER": certificate.get("NUMBER"),
                        "CERTIFICATE_START_DATE": certificate.get("DATE_START"),
                        "CERTIFICATE_END_DATA": certificate.get("DATE_END"),
                    } for certificate in certificates] if certificates.exists() else [],
                    "ORGANIZATION_CONTACTS": [{
                        "ID_PRODUCTS": contact.get("ID_PRODUCTS"),
                        "CONTACTS_PRODUCTS_NAME": contact.get("ID_PRODUCTS__PRODUCTS_NAME"),
                        "CONTACTS_NUMBER": contact.get("NUMBER"),
                    } for contact in contacts] if contacts.exists() else [],
                    "ORGANIZATION_DETAIL": [{
                        "DETAIL": detail.get("DETAIL"),
                    } for detail in details] if details.exists() else [],
                }
                self.display = True
                return return_data

    def def_get_organizations_messages(self):
        """获取所有组织信息"""
        self.data.clear()
        self.display = False
        organizations_data = TransactionEconomyIndustryOrganizationsBases.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1,
        ).values("ID", 'ENTERPRISE_NAME', 'ENTERPRISE_CODE__ABBREVIATION', "COUNTRY_CREATE_TIME", "COUNTRY_END_TIME")
        if organizations_data.exists():
            for organization_data in organizations_data:
                organization_id = organization_data.get("ID")
                calls = TransactionEconomyIndustryOrganizationsCall.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_ORGANIZATIONS=organization_id,
                ).values('ENTERPRISE_NAME_CODE__ABBREVIATION', 'ENTERPRISE_NAME', )
                address = TransactionEconomyIndustryOrganizationsAddress.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_ORGANIZATIONS=organization_id,
                ).values('ENTERPRISE_ADDRESS_CODE__ABBREVIATION', 'ENTERPRISE_ADDRESS_NAME', )
                details = TransactionEconomyIndustryOrganizationsDetails.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_ORGANIZATIONS=organization_id,
                ).values('DETAIL', )
                certificates = TransactionEconomyIndustryOrganizationsCertificate.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_ORGANIZATIONS=organization_id,
                ).values(
                    'SIGNING_AND_ISSUING_ORGANIZATION', "SIGNING_AND_ISSUING_ORGANIZATION__ENTERPRISE_NAME",
                    'DATE_ISSUED', "CODE__ABBREVIATION", "NUMBER", "DATE_START", "DATE_END",
                )
                contacts = TransactionEconomyIndustryOrganizationsContact.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_ORGANIZATIONS=organization_id,
                ).values('ID_PRODUCTS', 'ID_PRODUCTS__PRODUCTS_NAME', "NUMBER", )
                return_data = {
                    "ID_ORGANIZATION": organization_id,
                    "ORGANIZATION_NAME": organization_data.get('ENTERPRISE_NAME'),
                    "ORGANIZATION_URL": organization_data.get('ENTERPRISE_CODE__ABBREVIATION'),
                    "ORGANIZATION_CREATE_TIME": organization_data.get('COUNTRY_CREATE_TIME'),
                    "ORGANIZATION_END_TIME": organization_data.get('COUNTRY_END_TIME'),
                    "ORGANIZATION_CALLS": [{
                        "CALL_NAME": call.get("ENTERPRISE_NAME"),
                        "CALL_NAME_CODE": call.get("ENTERPRISE_NAME_CODE__ABBREVIATION"),
                    } for call in calls] if calls.exists() else [],
                    "ORGANIZATION_ADDRESS": [{
                        "ADDR_NAME": addr.get("ENTERPRISE_ADDRESS_NAME"),
                        "ADDR_NAME_CODE": addr.get("ENTERPRISE_ADDRESS_CODE__ABBREVIATION"),
                    } for addr in address] if address.exists() else [],
                    "ORGANIZATION_CERTIFICATES": [{
                        "CERTIFICATE_ISSUING": certificate.get("SIGNING_AND_ISSUING_ORGANIZATION"),
                        "CERTIFICATE_ISSUING_NAME": certificate.get(
                            "SIGNING_AND_ISSUING_ORGANIZATION__ENTERPRISE_NAME"),
                        "CERTIFICATE_ISSUED_DATA": certificate.get("DATE_ISSUED"),
                        "CERTIFICATE_CODE": certificate.get("CODE__ABBREVIATION"),
                        "CERTIFICATE_NUMBER": certificate.get("NUMBER"),
                        "CERTIFICATE_START_DATE": certificate.get("DATE_START"),
                        "CERTIFICATE_END_DATA": certificate.get("DATE_END"),
                    } for certificate in certificates] if certificates.exists() else [],
                    "ORGANIZATION_CONTACTS": [{
                        "ID_PRODUCTS": contact.get("ID_PRODUCTS"),
                        "CONTACTS_PRODUCTS_NAME": contact.get("ID_PRODUCTS__PRODUCTS_NAME"),
                        "CONTACTS_NUMBER": contact.get("NUMBER"),
                    } for contact in contacts] if contacts.exists() else [],
                    "ORGANIZATION_DETAIL": [{
                        "DETAIL": detail.get("DETAIL"),
                    } for detail in details] if details.exists() else [],
                }
                self.data.append(return_data)
                self.display = True

    def def_yield_get_organizations_messages(self):
        """yield 获取所有组织信息"""
        self.display = True
        organizations_data = TransactionEconomyIndustryOrganizationsBases.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1,
        ).values("ID", 'ENTERPRISE_NAME', 'ENTERPRISE_CODE__ABBREVIATION', "COUNTRY_CREATE_TIME", "COUNTRY_END_TIME")
        if organizations_data.exists():
            for organization_data in organizations_data:
                organization_id = organization_data.get("ID")
                calls = TransactionEconomyIndustryOrganizationsCall.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_ORGANIZATIONS=organization_id,
                ).values('ENTERPRISE_NAME_CODE__ABBREVIATION', 'ENTERPRISE_NAME', )
                address = TransactionEconomyIndustryOrganizationsAddress.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_ORGANIZATIONS=organization_id,
                ).values('ENTERPRISE_ADDRESS_CODE__ABBREVIATION', 'ENTERPRISE_ADDRESS_NAME', )
                details = TransactionEconomyIndustryOrganizationsDetails.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_ORGANIZATIONS=organization_id,
                ).values('DETAIL', )
                certificates = TransactionEconomyIndustryOrganizationsCertificate.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_ORGANIZATIONS=organization_id,
                ).values(
                    'SIGNING_AND_ISSUING_ORGANIZATION', "SIGNING_AND_ISSUING_ORGANIZATION__ENTERPRISE_NAME",
                    'DATE_ISSUED', "CODE__ABBREVIATION", "NUMBER", "DATE_START", "DATE_END",
                )
                contacts = TransactionEconomyIndustryOrganizationsContact.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_ORGANIZATIONS=organization_id,
                ).values('ID_PRODUCTS', 'ID_PRODUCTS__PRODUCTS_NAME', "NUMBER", )
                return_data = {
                    "ID_ORGANIZATION": organization_id,
                    "ORGANIZATION_NAME": organization_data.get('ENTERPRISE_NAME'),
                    "ORGANIZATION_URL": organization_data.get('ENTERPRISE_CODE__ABBREVIATION'),
                    "ORGANIZATION_CREATE_TIME": organization_data.get('COUNTRY_CREATE_TIME'),
                    "ORGANIZATION_END_TIME": organization_data.get('COUNTRY_END_TIME'),
                    "ORGANIZATION_CALLS": [{
                        "CALL_NAME": call.get("ENTERPRISE_NAME"),
                        "CALL_NAME_CODE": call.get("ENTERPRISE_NAME_CODE__ABBREVIATION"),
                    } for call in calls] if calls.exists() else [],
                    "ORGANIZATION_ADDRESS": [{
                        "ADDR_NAME": addr.get("ENTERPRISE_ADDRESS_NAME"),
                        "ADDR_NAME_CODE": addr.get("ENTERPRISE_ADDRESS_CODE__ABBREVIATION"),
                    } for addr in address] if address.exists() else [],
                    "ORGANIZATION_CERTIFICATES": [{
                        "CERTIFICATE_ISSUING": certificate.get("SIGNING_AND_ISSUING_ORGANIZATION"),
                        "CERTIFICATE_ISSUING_NAME": certificate.get(
                            "SIGNING_AND_ISSUING_ORGANIZATION__ENTERPRISE_NAME"),
                        "CERTIFICATE_ISSUED_DATA": certificate.get("DATE_ISSUED"),
                        "CERTIFICATE_CODE": certificate.get("CODE__ABBREVIATION"),
                        "CERTIFICATE_NUMBER": certificate.get("NUMBER"),
                        "CERTIFICATE_START_DATE": certificate.get("DATE_START"),
                        "CERTIFICATE_END_DATA": certificate.get("DATE_END"),
                    } for certificate in certificates] if certificates.exists() else [],
                    "ORGANIZATION_CONTACTS": [{
                        "ID_PRODUCTS": contact.get("ID_PRODUCTS"),
                        "CONTACTS_PRODUCTS_NAME": contact.get("ID_PRODUCTS__PRODUCTS_NAME"),
                        "CONTACTS_NUMBER": contact.get("NUMBER"),
                    } for contact in contacts] if contacts.exists() else [],
                    "ORGANIZATION_DETAIL": [{
                        "DETAIL": detail.get("DETAIL"),
                    } for detail in details] if details.exists() else [],
                }
                yield return_data
