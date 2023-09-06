from country.models import (
    TransactionGeographyPoliticsCountryCollect,
    TransactionGeographyPoliticsCountryCollectCall,
    TransactionGeographyPoliticsCountryCurrency
)


class CountryMessage(object):
    """获取国家信息"""

    def __init__(self, country_id=None):
        self.country_id = country_id
        self.display = False
        self.data = []

    @property
    def dict(self):
        return self.__dict__

    def get_country_message(self):
        """获取单个国家信息"""
        self.display = False
        if self.country_id:
            collect = TransactionGeographyPoliticsCountryCollect.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID=self.country_id,
            ).values('NAME', "TWO_CHARACTER_CODE", "THREE_CHARACTER_CODE", "NUMERIC_CODE", ).distinct()
            if collect.exists():
                collect = collect.first()

                collect_calls = TransactionGeographyPoliticsCountryCollectCall.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_NATION=self.country_id,
                ).values('NAME_CODE__ABBREVIATION', "NAME", )
                country_currency = TransactionGeographyPoliticsCountryCurrency.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_NATION=self.country_id,
                ).values(
                    'COUNTRY_DESCRIBE_CHINESE', "COUNTRY_DESCRIBE_ENGLISH", "COUNTRY_NOTATION", "COUNTRY_ISO_CODE",
                    "COUNTRY_AUXILIARY_UNIT", "COUNTRY_CARRY_SYSTEM", "DETAIL",
                )
                return_data = {
                    "ID_NATION": self.country_id,
                    "NATION_NAME": collect.get("NAME"),
                    "NATION_TWO": collect.get("TWO_CHARACTER_CODE"),
                    "NATION_THREE": collect.get("THREE_CHARACTER_CODE"),
                    "NATION_NUMERIC": collect.get("NUMERIC_CODE"),
                    "NATION_CALLS": [{
                        collect_call.get("NAME_CODE__ABBREVIATION"): collect_call.get("NAME")}
                        for collect_call in collect_calls] if collect_calls.exists() else None,
                    "COUNTRY": [{
                        "COUNTRY_CHINESE": currency.get("COUNTRY_DESCRIBE_CHINESE"),
                        "COUNTRY_ENGLISH": currency.get("COUNTRY_DESCRIBE_ENGLISH"),
                        "COUNTRY_NOTATION": currency.get("COUNTRY_NOTATION"),
                        "COUNTRY_ISO": currency.get("COUNTRY_ISO_CODE"),
                        "COUNTRY_UNIT": currency.get("COUNTRY_AUXILIARY_UNIT"),
                        "COUNTRY_CARRY": currency.get("COUNTRY_CARRY_SYSTEM"),
                        "DETAIL": currency.get("DETAIL")}
                        for currency in country_currency] if country_currency.exists() else None,
                }
                self.display = True
                return return_data

    def get_country_messages(self):
        """获取所有国家信息"""
        self.display = False
        self.data.clear()
        collects = TransactionGeographyPoliticsCountryCollect.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1,
        ).values('ID', 'NAME', "TWO_CHARACTER_CODE", "THREE_CHARACTER_CODE", "NUMERIC_CODE", )
        if collects.exists():
            for collect in collects:
                collect_id = collect.get("ID").hex
                return_collect_data = {
                    "ID_NATION": collect_id,
                    "NATION_NAME": collect.get("NAME"),
                    "NATION_TWO": collect.get("TWO_CHARACTER_CODE"),
                    "NATION_THREE": collect.get("THREE_CHARACTER_CODE"),
                    "NATION_NUMERIC": collect.get("NUMERIC_CODE"),
                }

                collect_calls = TransactionGeographyPoliticsCountryCollectCall.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_NATION=collect_id,
                ).values('NAME_CODE__ABBREVIATION', "NAME", ).distinct()
                return_collect_data.update({"NATION_CALLS": [{
                    collect_call.get("NAME_CODE__ABBREVIATION"): collect_call.get("NAME")}
                    for collect_call in collect_calls]} if collect_calls.exists() else None)
                country_currency = TransactionGeographyPoliticsCountryCurrency.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_NATION=collect_id,
                ).values(
                    'COUNTRY_DESCRIBE_CHINESE', "COUNTRY_DESCRIBE_ENGLISH", "COUNTRY_NOTATION", "COUNTRY_ISO_CODE",
                    "COUNTRY_AUXILIARY_UNIT", "COUNTRY_CARRY_SYSTEM", "DETAIL",
                ).distinct()
                return_collect_data.update({
                    "COUNTRY": [{
                        "COUNTRY_CHINESE": currency.get("COUNTRY_DESCRIBE_CHINESE"),
                        "COUNTRY_ENGLISH": currency.get("COUNTRY_DESCRIBE_ENGLISH"),
                        "COUNTRY_NOTATION": currency.get("COUNTRY_NOTATION"),
                        "COUNTRY_ISO": currency.get("COUNTRY_ISO_CODE"),
                        "COUNTRY_UNIT": currency.get("COUNTRY_AUXILIARY_UNIT"),
                        "COUNTRY_CARRY": currency.get("COUNTRY_CARRY_SYSTEM"),
                        "DETAIL": currency.get("DETAIL")}
                        for currency in country_currency] if country_currency.exists() else None})
                self.data.append(return_collect_data)
            self.display = True

    def get_country_yield_messages(self):
        """yield 获取所有国家信息"""
        self.data.clear()
        collects = TransactionGeographyPoliticsCountryCollect.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1,
        ).values('ID', 'NAME', "TWO_CHARACTER_CODE", "THREE_CHARACTER_CODE", "NUMERIC_CODE", )
        if collects.exists():
            for collect in collects:
                collect_id = collect.get("ID").hex
                return_collect_data = {
                    "ID_NATION": collect_id,
                    "NATION_NAME": collect.get("NAME"),
                    "NATION_TWO": collect.get("TWO_CHARACTER_CODE"),
                    "NATION_THREE": collect.get("THREE_CHARACTER_CODE"),
                    "NATION_NUMERIC": collect.get("NUMERIC_CODE"),
                }

                collect_calls = TransactionGeographyPoliticsCountryCollectCall.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_NATION=collect_id,
                ).values('NAME_CODE__ABBREVIATION', "NAME", ).distinct()
                return_collect_data.update({"NATION_CALLS": [{
                    collect_call.get("NAME_CODE__ABBREVIATION"): collect_call.get("NAME")}
                    for collect_call in collect_calls]} if collect_calls.exists() else None)
                country_currency = TransactionGeographyPoliticsCountryCurrency.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_NATION=collect_id,
                ).values(
                    'COUNTRY_DESCRIBE_CHINESE', "COUNTRY_DESCRIBE_ENGLISH", "COUNTRY_NOTATION", "COUNTRY_ISO_CODE",
                    "COUNTRY_AUXILIARY_UNIT", "COUNTRY_CARRY_SYSTEM", "DETAIL",
                ).distinct()
                return_collect_data.update({
                    "COUNTRY": [{
                        "COUNTRY_CHINESE": currency.get("COUNTRY_DESCRIBE_CHINESE"),
                        "COUNTRY_ENGLISH": currency.get("COUNTRY_DESCRIBE_ENGLISH"),
                        "COUNTRY_NOTATION": currency.get("COUNTRY_NOTATION"),
                        "COUNTRY_ISO": currency.get("COUNTRY_ISO_CODE"),
                        "COUNTRY_UNIT": currency.get("COUNTRY_AUXILIARY_UNIT"),
                        "COUNTRY_CARRY": currency.get("COUNTRY_CARRY_SYSTEM"),
                        "DETAIL": currency.get("DETAIL")}
                        for currency in country_currency] if country_currency.exists() else None})
                yield return_collect_data
            self.display = True
