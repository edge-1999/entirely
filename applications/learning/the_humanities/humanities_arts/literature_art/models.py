from django.db import models

from simplepro.components import fields
from simplepro.editor import fields as editor_fields

from docs.utils.model_communal.model_communal import BasesModelCommunalId
from docs.utils.model_communal.model_queryset import get_queryset_literature_art_content_type


# Create your models here.

# 文字艺术
class LearningTheHumanitiesHumanitiesArtsLiteratureArtContent(BasesModelCommunalId):
    """文字艺术"""
    CONTENT = editor_fields.MDTextField(
        verbose_name="文字内容", default=None, blank=False, null=False, unique=True)

    class Meta:
        db_table = "LearningTheHumanitiesHumanitiesArtsLiteratureArtContent"
        ordering = ['-CREATE_TIME']
        verbose_name = "文字艺术"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.CONTENT[:100]}'


# 文字艺术类别
class LearningTheHumanitiesHumanitiesArtsLiteratureArtContentType(BasesModelCommunalId):
    """文字艺术类别"""
    LITERATURE_ART_ID = fields.ForeignKey(
        'literature_art.LearningTheHumanitiesHumanitiesArtsLiteratureArtContent', verbose_name='文字内容',
        on_delete=models.CASCADE, null=True, blank=True, to_field='ID', clearable=True, placeholder='文字内容', )
    LITERATURE_ART_CODE = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='文字艺术类别',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='文字艺术类别',
        queryset=get_queryset_literature_art_content_type,
    )

    class Meta:
        db_table = "LearningTheHumanitiesHumanitiesArtsLiteratureArtContentType"
        ordering = ['-CREATE_TIME']
        verbose_name = "文字艺术类别"
        verbose_name_plural = verbose_name
        unique_together = ('LITERATURE_ART_ID', 'LITERATURE_ART_CODE',)

    def __str__(self):
        return f'{self.ID.hex}'
