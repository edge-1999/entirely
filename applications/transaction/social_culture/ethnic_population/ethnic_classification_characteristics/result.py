from ethnic_classification_characteristics.models import (
    TransactionSocialCultureEthnicPopulationEthnicClassificationCharacteristicsBrief
)


class BriefMessage(object):
    """获取民族信息"""

    def __init__(self, brief_id=None):
        self.brief_id = brief_id
        self.NAME = None
        self.DETAIL = None
        self.display = False
        self.data = []

    def gef_get_brief_message(self):
        """获取单个民族信息"""
        self.display = False
        if self.brief_id:
            briefs = TransactionSocialCultureEthnicPopulationEthnicClassificationCharacteristicsBrief.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID=self.brief_id,
            ).values('ID', 'NAME', "DETAIL", ).distinct()
            if briefs.exists():
                briefs = briefs.first()
                self.NAME = briefs.get("NAME")
                self.DETAIL = briefs.get("DETAIL")
                self.display = True

    def gef_get_briefs_message(self):
        """获取所有民族信息"""
        self.display = False
        if self.brief_id:
            briefs = TransactionSocialCultureEthnicPopulationEthnicClassificationCharacteristicsBrief.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1,
            ).values('ID', 'NAME', "DETAIL", ).distinct()
            if briefs.exists():
                for brief in briefs:
                    brief_list_data = {
                        "ID": brief.get("ID"),
                        "NAME": brief.get("NAME"),
                        "DETAIL": brief.get("DETAIL"),
                    }
                    self.data.append(brief_list_data)
                self.display = True

    @property
    def gef_get_yield_briefs_message(self):
        """通过生成器获取所有的民族信息"""
        if self.brief_id:
            briefs = TransactionSocialCultureEthnicPopulationEthnicClassificationCharacteristicsBrief.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1,
            ).values('ID', 'NAME', "DETAIL", ).distinct()
            if briefs.exists():
                for brief in briefs:
                    brief_list_data = {
                        "ID": brief.get("ID"),
                        "NAME": brief.get("NAME"),
                        "DETAIL": brief.get("DETAIL"),
                    }
                    yield brief_list_data
