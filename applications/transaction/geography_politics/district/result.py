from country.result import CountryMessage
from district.models import TransactionGeographyPoliticsDistrictBasic


class DistrictMessage(object):
    """城镇信息"""

    def __init__(self, district_id=None):
        self.district_id = district_id
        self.display = False
        self.data = []

    def get_district_message(self):
        """获取单个城镇信息"""
        self.display = False
        if self.district_id:
            district_message = TransactionGeographyPoliticsDistrictBasic.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID=self.district_id,
            ).values(
                'ID_NATION', 'TYPE_TOWN__ABBREVIATION', 'NAME_CHINESE', "NAME_ENGLISH", "ID_SUBORDINATE", "ID_PARENT",
            ).distinct()
            if district_message.exists():
                district_message = district_message.first()
                country = CountryMessage(district_message.get("ID_NATION"))
                country_data = country.get_country_message()
                return_district_data = {
                    "ID_DISTRICT": self.district_id,
                    "DISTRICT_ID_PARENT": district_message.get("ID_PARENT"),
                    "DISTRICT_SUBORDINATE": district_message.get("ID_SUBORDINATE"),
                    "DISTRICT_NAME_CHINESE": district_message.get("NAME_CHINESE"),
                    "DISTRICT_NAME_ENGLISH": district_message.get("NAME_ENGLISH"),
                    "DISTRICT_NATION": country_data if country.display else None,
                    "DISTRICT_TOWN": district_message.get("TYPE_TOWN__ABBREVIATION"),
                    "DISTRICT_COUNTRY": district_message.get("TYPE_TOWN__ABBREVIATION"),
                }
                self.display = True
                return return_district_data

    def get_district_messages(self):
        """获取所有城镇信息"""
        self.display = False
        self.data.clear()
        district_messages = TransactionGeographyPoliticsDistrictBasic.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1,
        ).values(
            'ID_NATION', 'TYPE_TOWN__ABBREVIATION', 'NAME_CHINESE', "NAME_ENGLISH", "ID_SUBORDINATE", "ID_PARENT",
        ).distinct()
        if district_messages.exists():
            for district_message in district_messages:
                country = CountryMessage(district_message.get("ID_NATION"))
                country_data = country.get_country_message()
                return_district_data = {
                    "ID_DISTRICT": self.district_id,
                    "DISTRICT_ID_PARENT": district_message.get("ID_PARENT"),
                    "DISTRICT_SUBORDINATE": district_message.get("ID_SUBORDINATE"),
                    "DISTRICT_NAME_CHINESE": district_message.get("NAME_CHINESE"),
                    "DISTRICT_NAME_ENGLISH": district_message.get("NAME_ENGLISH"),
                    "DISTRICT_NATION": country_data if country.display else None,
                    "DISTRICT_TOWN": district_message.get("TYPE_TOWN__ABBREVIATION"),
                    "DISTRICT_COUNTRY": district_message.get("TYPE_TOWN__ABBREVIATION"),
                }
                self.data.append(return_district_data)
            self.display = True
            return self.data

    def get_yield_district_messages(self):
        """ yield 获取所有城镇信息"""
        district_messages = TransactionGeographyPoliticsDistrictBasic.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1,
        ).values(
            'ID_NATION', 'TYPE_TOWN__ABBREVIATION', 'NAME_CHINESE', "NAME_ENGLISH", "ID_SUBORDINATE", "ID_PARENT",
        ).distinct()
        if district_messages.exists():
            for district_message in district_messages:
                country = CountryMessage(district_message.get("ID_NATION"))
                country_data = country.get_country_message()
                return_district_data = {
                    "ID_DISTRICT": self.district_id,
                    "DISTRICT_ID_PARENT": district_message.get("ID_PARENT"),
                    "DISTRICT_SUBORDINATE": district_message.get("ID_SUBORDINATE"),
                    "DISTRICT_NAME_CHINESE": district_message.get("NAME_CHINESE"),
                    "DISTRICT_NAME_ENGLISH": district_message.get("NAME_ENGLISH"),
                    "DISTRICT_NATION": country_data if country.display else None,
                    "DISTRICT_TOWN": district_message.get("TYPE_TOWN__ABBREVIATION"),
                    "DISTRICT_COUNTRY": district_message.get("TYPE_TOWN__ABBREVIATION"),
                }
                yield return_district_data
