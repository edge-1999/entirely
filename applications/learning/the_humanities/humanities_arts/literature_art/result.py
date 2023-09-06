from literature_art.models import LearningTheHumanitiesHumanitiesArtsLiteratureArtContentType


class LiteratureArt(object):
    def __init__(self, literature_art_id=None, literature_code=None):
        self.literature_art_id = literature_art_id
        self.literature_code = literature_code
        self.display = False
        self.data = []
        if self.literature_art_id and not self.literature_code:
            self.__get_literature_id_data()
        elif self.literature_code and not self.literature_art_id:
            self.__get_literature_code_data()

    def __get_literature_data(self):
        """获取所有的文字"""
        self.data.clear()
        literatures = LearningTheHumanitiesHumanitiesArtsLiteratureArtContentType.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1,
        ).values('LITERATURE_ART_CODE__ABBREVIATION', "LITERATURE_ART_CODE__TECHNOLOGY", "LITERATURE_ART_ID")
        if literatures.exists():
            for literature in literatures:
                return_data = {
                    "LITERATURE_ID": literature.get("LITERATURE_ART_ID"),
                    "LITERATURE_CODE": literature.get("LITERATURE_ART_CODE__TECHNOLOGY"),
                    "LITERATURE_CODE_NAME": literature.get("LITERATURE_ART_CODE__ABBREVIATION"),
                }
                self.data.append(return_data)
                self.display = True

    def __get_literature_id_data(self):
        self.data.clear()
        literatures = LearningTheHumanitiesHumanitiesArtsLiteratureArtContentType.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, LITERATURE_ART_ID=self.literature_art_id,
        ).values('LITERATURE_ART_CODE__ABBREVIATION', "LITERATURE_ART_CODE__TECHNOLOGY", "LITERATURE_ART_ID")
        if literatures.exists():
            for literature in literatures:
                return_data = {
                    "LITERATURE_ID": literature.get("LITERATURE_ART_ID"),
                    "LITERATURE_CODE": literature.get("LITERATURE_ART_CODE__TECHNOLOGY"),
                    "LITERATURE_CODE_NAME": literature.get("LITERATURE_ART_CODE__ABBREVIATION"),
                }
                self.data.append(return_data)
                self.display = True

    def __get_literature_code_data(self):
        self.data.clear()
        literatures = LearningTheHumanitiesHumanitiesArtsLiteratureArtContentType.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, LITERATURE_ART_CODE=self.literature_code,
        ).values('LITERATURE_ART_CODE__ABBREVIATION', "LITERATURE_ART_CODE__TECHNOLOGY", "LITERATURE_ART_ID")
        if literatures.exists():
            for literature in literatures:
                return_data = {
                    "LITERATURE_ID": literature.get("LITERATURE_ART_ID"),
                    "LITERATURE_CODE": literature.get("LITERATURE_ART_CODE__TECHNOLOGY"),
                    "LITERATURE_CODE_NAME": literature.get("LITERATURE_ART_CODE__ABBREVIATION"),
                }
                self.data.append(return_data)
                self.display = True
