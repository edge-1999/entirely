from country.result import CountryMessage
from personal_Information.models import (
    TransactionSocialCultureEthnicPopulationPersonalInformationPerson,
    TransactionSocialCultureEthnicPopulationPersonalInformationPersonNation,
    TransactionSocialCultureEthnicPopulationPersonalInformationPersonCountry,
    TransactionSocialCultureEthnicPopulationPersonalInformationPersonBirthday,
    TransactionSocialCultureEthnicPopulationPersonalInformationPersonAddress,
    TransactionSocialCultureEthnicPopulationPersonalInformationPersonConnections,
    TransactionSocialCultureEthnicPopulationPersonalInformationPersonCertificate
)


class PersonMessage(object):
    """获取个人信息"""

    def __init__(self, person_id=None):
        self.person_id = person_id
        self.display = False
        self.data = []
        self.def_get_person_message()

    def def_get_person_message(self):
        """获取单个人员基础信息"""
        self.display = False
        if self.person_id:
            persons = TransactionSocialCultureEthnicPopulationPersonalInformationPerson.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID=self.person_id,
            ).values('ID', 'SURNAME', "NAME", "SEX__ABBREVIATION", "DATE_OF_DEATH", "DETAIL").distinct()
            if persons.exists():
                persons = persons.first()
                briefs = TransactionSocialCultureEthnicPopulationPersonalInformationPersonCountry.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PERSON=self.person_id,
                ).values('ID_NATION', "DATE_OF_DEATH").distinct()
                nations_data_list = []
                if briefs.exists():
                    for brief in briefs:
                        brief_data = CountryMessage(brief.get("ID").hex).get_country_message()
                        country_message = brief_data
                        if brief_data.display:
                            nations_data_list.append(country_message)
                birthdays = TransactionSocialCultureEthnicPopulationPersonalInformationPersonBirthday.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PERSON=self.person_id,
                ).values('TYPE_BIRTHDAY__ABBREVIATION', "DATE_START").distinct()
                address = TransactionSocialCultureEthnicPopulationPersonalInformationPersonAddress.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PERSON=self.person_id,
                ).values('TYPE_ADDRESS__ABBREVIATION', "ADDRESS_TXT").distinct()
                TransactionSocialCultureEthnicPopulationPersonalInformationPersonNation.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PERSON=self.person_id,
                ).values('ID_NATION').distinct()
                connections = TransactionSocialCultureEthnicPopulationPersonalInformationPersonConnections.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PERSON=self.person_id,
                ).values('ID_PRODUCTS', 'ID_PRODUCTS__PRODUCTS_NAME', "NUMBER").distinct()
                certificates = TransactionSocialCultureEthnicPopulationPersonalInformationPersonCertificate.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PERSON=self.person_id,
                ).values(
                    'CODE__ABBREVIATION', 'NUMBER', "ID_ORGANIZATIONS", "ID_ORGANIZATIONS__ENTERPRISE_NAME",
                    'DATE_ISSUED', 'DATE_START', 'DATE_END',
                ).distinct()
                return_person_data = {
                    "ID_PERSON": self.person_id,
                    "PERSON_SURNAME": persons.get("SURNAME"),
                    "PERSON_NAME": persons.get("NAME"),
                    "PERSON_SEX": persons.get("SEX__ABBREVIATION"),
                    "PERSON_OF_DATA": persons.get("DATE_OF_DEATH"),
                    "PERSON_NATION": nations_data_list,
                    "PERSON_BIRTHDAY": [{
                        "BIRTHDAY_TYPE": birthday.get("TYPE_BIRTHDAY__ABBREVIATION"),
                        "BIRTHDAY_START_DATE": birthday.get("DATE_START"),
                    } for birthday in birthdays] if birthdays.exists() else [],
                    "PERSON_ADDRESS": [{
                        "ADDRESS_TYPE": addr.get("TYPE_ADDRESS__ABBREVIATION"),
                        "ADDRESS_TXT": addr.get("ADDRESS_TXT"),
                    } for addr in address] if address.exists() else [],
                    "PERSON_CONNECTIONS": [{
                        "ID_PRODUCTS": connection.get('ID_PRODUCTS'),
                        "PRODUCTS_NAME": connection.get('ID_PRODUCTS__PRODUCTS_NAME'),
                        "NUMBER": connection.get('NUMBER'),
                    } for connection in connections] if connections.exists() else [],
                    "PERSON_CERTIFICATES": [{
                        "CODE": certificate.get("CODE__ABBREVIATION"),
                        "NUMBER": certificate.get("NUMBER"),
                        "ID_ORGANIZATIONS": certificate.get("ID_ORGANIZATIONS"),
                        "ORGANIZATIONS_NAME": certificate.get("ID_ORGANIZATIONS__ENTERPRISE_NAME"),
                        "DATE_ISSUED": certificate.get("DATE_ISSUED"),
                        "DATE_START": certificate.get("DATE_START"),
                        "DATE_END": certificate.get("DATE_END"),
                    } for certificate in certificates] if certificates.exists() else [],
                }
                self.display = True
                return return_person_data

    def def_get_person_messages(self):
        """获取所有人员基础信息"""
        self.display = False
        self.data.clear()
        persons_data_ = TransactionSocialCultureEthnicPopulationPersonalInformationPerson.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1,
        ).values('ID', 'SURNAME', "NAME", "SEX__ABBREVIATION", "DATE_OF_DEATH", "DETAIL").distinct()
        if persons_data_.exists():
            for persons in persons_data_:
                briefs = TransactionSocialCultureEthnicPopulationPersonalInformationPersonCountry.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PERSON=self.person_id,
                ).values('ID_NATION', "DATE_OF_DEATH").distinct()
                nations_data_list = []
                if briefs.exists():
                    for brief in briefs:
                        brief_data = CountryMessage(brief.get("ID").hex).get_country_message()
                        country_message = brief_data
                        if brief_data.display:
                            nations_data_list.append(country_message)
                birthdays = TransactionSocialCultureEthnicPopulationPersonalInformationPersonBirthday.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PERSON=self.person_id,
                ).values('TYPE_BIRTHDAY__ABBREVIATION', "DATE_START").distinct()
                address = TransactionSocialCultureEthnicPopulationPersonalInformationPersonAddress.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PERSON=self.person_id,
                ).values('TYPE_ADDRESS__ABBREVIATION', "ADDRESS_TXT").distinct()
                TransactionSocialCultureEthnicPopulationPersonalInformationPersonNation.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PERSON=self.person_id,
                ).values('ID_NATION').distinct()
                connections = TransactionSocialCultureEthnicPopulationPersonalInformationPersonConnections.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PERSON=self.person_id,
                ).values('ID_PRODUCTS', 'ID_PRODUCTS__PRODUCTS_NAME', "NUMBER").distinct()
                certificates = TransactionSocialCultureEthnicPopulationPersonalInformationPersonCertificate.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PERSON=self.person_id,
                ).values(
                    'CODE__ABBREVIATION', 'NUMBER', "ID_ORGANIZATIONS", "ID_ORGANIZATIONS__ENTERPRISE_NAME",
                    'DATE_ISSUED', 'DATE_START', 'DATE_END',
                ).distinct()
                return_person_data = {
                    "ID_PERSON": self.person_id,
                    "PERSON_SURNAME": persons.get("SURNAME"),
                    "PERSON_NAME": persons.get("NAME"),
                    "PERSON_SEX": persons.get("SEX__ABBREVIATION"),
                    "PERSON_OF_DATA": persons.get("DATE_OF_DEATH"),
                    "PERSON_NATION": nations_data_list,
                    "PERSON_BIRTHDAY": [{
                        "BIRTHDAY_TYPE": birthday.get("TYPE_BIRTHDAY__ABBREVIATION"),
                        "BIRTHDAY_START_DATE": birthday.get("DATE_START"),
                    } for birthday in birthdays] if birthdays.exists() else [],
                    "PERSON_ADDRESS": [{
                        "ADDRESS_TYPE": addr.get("TYPE_ADDRESS__ABBREVIATION"),
                        "ADDRESS_TXT": addr.get("ADDRESS_TXT"),
                    } for addr in address] if address.exists() else [],
                    "PERSON_CONNECTIONS": [{
                        "ID_PRODUCTS": connection.get('ID_PRODUCTS'),
                        "PRODUCTS_NAME": connection.get('ID_PRODUCTS__PRODUCTS_NAME'),
                        "NUMBER": connection.get('NUMBER'),
                    } for connection in connections] if connections.exists() else [],
                    "PERSON_CERTIFICATES": [{
                        "CODE": certificate.get("CODE__ABBREVIATION"),
                        "NUMBER": certificate.get("NUMBER"),
                        "ID_ORGANIZATIONS": certificate.get("ID_ORGANIZATIONS"),
                        "ORGANIZATIONS_NAME": certificate.get("ID_ORGANIZATIONS__ENTERPRISE_NAME"),
                        "DATE_ISSUED": certificate.get("DATE_ISSUED"),
                        "DATE_START": certificate.get("DATE_START"),
                        "DATE_END": certificate.get("DATE_END"),
                    } for certificate in certificates] if certificates.exists() else [],
                }
                self.data.append(return_person_data)
            self.display = True

    def def_yield_get_person_messages(self):
        """yield 获取所有人员基础信息"""
        persons_data_ = TransactionSocialCultureEthnicPopulationPersonalInformationPerson.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1,
        ).values('ID', 'SURNAME', "NAME", "SEX__ABBREVIATION", "DATE_OF_DEATH", "DETAIL").distinct()
        if persons_data_.exists():
            for persons in persons_data_:
                briefs = TransactionSocialCultureEthnicPopulationPersonalInformationPersonCountry.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PERSON=self.person_id,
                ).values('ID_NATION', "DATE_OF_DEATH").distinct()
                nations_data_list = []
                if briefs.exists():
                    for brief in briefs:
                        brief_data = CountryMessage(brief.get("ID").hex).get_country_message()
                        country_message = brief_data
                        if brief_data.display:
                            nations_data_list.append(country_message)
                birthdays = TransactionSocialCultureEthnicPopulationPersonalInformationPersonBirthday.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PERSON=self.person_id,
                ).values('TYPE_BIRTHDAY__ABBREVIATION', "DATE_START").distinct()
                address = TransactionSocialCultureEthnicPopulationPersonalInformationPersonAddress.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PERSON=self.person_id,
                ).values('TYPE_ADDRESS__ABBREVIATION', "ADDRESS_TXT").distinct()
                TransactionSocialCultureEthnicPopulationPersonalInformationPersonNation.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PERSON=self.person_id,
                ).values('ID_NATION').distinct()
                connections = TransactionSocialCultureEthnicPopulationPersonalInformationPersonConnections.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PERSON=self.person_id,
                ).values('ID_PRODUCTS', 'ID_PRODUCTS__PRODUCTS_NAME', "NUMBER").distinct()
                certificates = TransactionSocialCultureEthnicPopulationPersonalInformationPersonCertificate.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PERSON=self.person_id,
                ).values(
                    'CODE__ABBREVIATION', 'NUMBER', "ID_ORGANIZATIONS", "ID_ORGANIZATIONS__ENTERPRISE_NAME",
                    'DATE_ISSUED', 'DATE_START', 'DATE_END',
                ).distinct()
                return_person_data = {
                    "ID_PERSON": self.person_id,
                    "PERSON_SURNAME": persons.get("SURNAME"),
                    "PERSON_NAME": persons.get("NAME"),
                    "PERSON_SEX": persons.get("SEX__ABBREVIATION"),
                    "PERSON_OF_DATA": persons.get("DATE_OF_DEATH"),
                    "PERSON_NATION": nations_data_list,
                    "PERSON_BIRTHDAY": [{
                        "BIRTHDAY_TYPE": birthday.get("TYPE_BIRTHDAY__ABBREVIATION"),
                        "BIRTHDAY_START_DATE": birthday.get("DATE_START"),
                    } for birthday in birthdays] if birthdays.exists() else [],
                    "PERSON_ADDRESS": [{
                        "ADDRESS_TYPE": addr.get("TYPE_ADDRESS__ABBREVIATION"),
                        "ADDRESS_TXT": addr.get("ADDRESS_TXT"),
                    } for addr in address] if address.exists() else [],
                    "PERSON_CONNECTIONS": [{
                        "ID_PRODUCTS": connection.get('ID_PRODUCTS'),
                        "PRODUCTS_NAME": connection.get('ID_PRODUCTS__PRODUCTS_NAME'),
                        "NUMBER": connection.get('NUMBER'),
                    } for connection in connections] if connections.exists() else [],
                    "PERSON_CERTIFICATES": [{
                        "CODE": certificate.get("CODE__ABBREVIATION"),
                        "NUMBER": certificate.get("NUMBER"),
                        "ID_ORGANIZATIONS": certificate.get("ID_ORGANIZATIONS"),
                        "ORGANIZATIONS_NAME": certificate.get("ID_ORGANIZATIONS__ENTERPRISE_NAME"),
                        "DATE_ISSUED": certificate.get("DATE_ISSUED"),
                        "DATE_START": certificate.get("DATE_START"),
                        "DATE_END": certificate.get("DATE_END"),
                    } for certificate in certificates] if certificates.exists() else [],
                }
                yield return_person_data
