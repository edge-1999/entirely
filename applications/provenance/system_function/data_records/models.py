from django.db import models
from simplepro.components import fields

from docs.utils.model_communal.model_communal import BasesModelCommunalId, BasesModelCommunal
from docs.utils.model_communal.model_queryset import (
    get_queryset_project_server_code,
    get_queryset_file_object_code,
    get_queryset_file_object_inherit_code
)


# Create your models here.
# 账户系统
class ProvenanceSystemFunctionDataRecordsSystem(BasesModelCommunalId):
    """账户系统"""
    ID_SUBSCRIBER = fields.ForeignKey(
        'account_management.ProvenanceSystemSettingsAccountManagementSubscriber', verbose_name='订阅用户',
        on_delete=models.CASCADE, null=False, blank=False, to_field='ID', clearable=True, placeholder='订阅用户', )
    ID_UNIQUE = fields.CharField(verbose_name='唯一标识', max_length=255, blank=True, null=True, show_word_limit=True)
    SYSTEM_CATEGORY = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='所属系统',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='所属系统',
        queryset=get_queryset_project_server_code, )
    NAME = fields.CharField(verbose_name='系统名称', max_length=255, blank=True, null=True, show_word_limit=True)

    class Meta:
        db_table = "ProvenanceSystemFunctionDataRecordsSystem"
        ordering = ['-CREATE_TIME']
        verbose_name = "账户系统表"
        verbose_name_plural = verbose_name
        unique_together = ('ID_SUBSCRIBER', 'ID_UNIQUE', 'SYSTEM_CATEGORY', 'NAME',)

    def __str__(self):
        return f'{self.ID_SUBSCRIBER}:{self.NAME}'


# 工作目录
class ProvenanceSystemFunctionDataRecordsSystemFolder(BasesModelCommunalId):
    """工作目录"""
    ID_SYSTEM = fields.ForeignKey(
        'data_records.ProvenanceSystemFunctionDataRecordsSystem', verbose_name='账户系统', on_delete=models.CASCADE,
        null=False, blank=False, to_field='ID', clearable=True, placeholder='账户系统', )
    INODE = fields.CharField(verbose_name='工作目录标识', max_length=255, blank=True, null=True, show_word_limit=True)
    NAME = fields.CharField(verbose_name='工作目录名称', max_length=255, blank=True, null=True, show_word_limit=True)
    PATH = fields.CharField(verbose_name='工作目录路径', max_length=255, blank=True, null=True, show_word_limit=True)

    class Meta:
        db_table = "ProvenanceSystemFunctionDataRecordsSystemFolder"
        ordering = ['-CREATE_TIME']
        verbose_name = "工作目录"
        verbose_name_plural = verbose_name
        unique_together = ('ID_SYSTEM', 'INODE',)

    def __str__(self):
        return f'{self.ID_SYSTEM}{self.NAME}'


# 文件对象
class ProvenanceSystemFunctionDataRecordsSystemFileObject(BasesModelCommunal):
    """文件对象"""
    ID_PARENT = fields.TreeComboboxField(
        'data_records.ProvenanceSystemFunctionDataRecordsSystemFileObject', on_delete=models.CASCADE, null=True,
        blank=True, verbose_name='上级', to_field='id', strictly=True, )
    ID_FOLDER = fields.ForeignKey(
        'data_records.ProvenanceSystemFunctionDataRecordsSystemFolder', verbose_name='工作目录',
        on_delete=models.CASCADE, null=False, blank=False, to_field='ID', clearable=True, placeholder='工作目录', )
    INODE = fields.CharField(verbose_name='工作目录标识', max_length=255, blank=True, null=True, show_word_limit=True)
    NAME = fields.CharField(verbose_name='工作目录名称', max_length=255, blank=True, null=True, show_word_limit=True)
    PATH = fields.CharField(verbose_name='工作目录路径', max_length=255, blank=True, null=True, show_word_limit=True)
    TYPE = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='对象类型',
        placeholder='对象类型', on_delete=models.CASCADE, null=False, blank=False, to_field='id', clearable=True,
        queryset=get_queryset_file_object_code, )

    class Meta:
        db_table = "ProvenanceSystemFunctionDataRecordsSystemFileObject"
        ordering = ['-CREATE_TIME']
        verbose_name = "文件对象"
        verbose_name_plural = verbose_name
        unique_together = ('ID_FOLDER', 'INODE',)

    def __str__(self):
        return f'{self.ID_FOLDER}{self.NAME}'


# 文件对象继承配置
class ProvenanceSystemFunctionDataRecordsSystemFileObjectInherit(BasesModelCommunalId):
    """文件对象继承配置"""
    ID_FILE_OBJECT = fields.ForeignKey(
        'data_records.ProvenanceSystemFunctionDataRecordsSystemFileObject', verbose_name='文件对象',
        on_delete=models.CASCADE, null=False, blank=False, to_field='id', clearable=True, placeholder='文件对象', )
    INHERIT_TYPE = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='继承类型',
        on_delete=models.CASCADE, null=False, blank=False, to_field='id', clearable=True, placeholder='继承类型',
        queryset=get_queryset_file_object_inherit_code, )
    INHERIT_VALUE = models.BooleanField(verbose_name="继承值", default=True, blank=False, null=False)

    class Meta:
        db_table = "ProvenanceSystemFunctionDataRecordsSystemFileObjectInherit"
        ordering = ['-CREATE_TIME']
        verbose_name = "文件对象继承配置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_FILE_OBJECT}'


class ProvenanceSystemFunctionDataRecordsTagTitle(BasesModelCommunalId):
    """标签主题"""
    ID_FOLDER = fields.ForeignKey(
        'data_records.ProvenanceSystemFunctionDataRecordsSystemFolder', verbose_name='工作目录',
        on_delete=models.CASCADE, null=False, blank=False, to_field='ID', clearable=True, placeholder='工作目录', )
    NAME = fields.CharField(verbose_name='主题名称', max_length=255, blank=False, null=False, show_word_limit=True)

    class Meta:
        db_table = "ProvenanceSystemFunctionDataRecordsTagTitle"
        ordering = ['-CREATE_TIME']
        verbose_name = "标签主题"
        verbose_name_plural = verbose_name
        unique_together = ('ID_FOLDER', 'NAME',)

    def __str__(self):
        return f'{self.NAME}'


# 标签
class ProvenanceSystemFunctionDataRecordsTag(BasesModelCommunalId):
    """标签"""
    ID_FOLDER = fields.ForeignKey(
        'data_records.ProvenanceSystemFunctionDataRecordsSystemFolder', verbose_name='工作目录',
        on_delete=models.CASCADE, null=True, blank=True, to_field='ID', clearable=True, placeholder='工作目录', )
    NAME = fields.CharField(
        verbose_name='标签名称', max_length=255, blank=False, null=False, show_word_limit=True)

    class Meta:
        db_table = "ProvenanceSystemFunctionDataRecordsTag"
        ordering = ['-CREATE_TIME']
        verbose_name = "文件对象"
        verbose_name_plural = verbose_name
        unique_together = ('ID_FOLDER', 'NAME',)

    def __str__(self):
        return f'{self.NAME}'


class ProvenanceSystemFunctionDataRecordsTagTitleTag(BasesModelCommunalId):
    """主题关联标签"""
    ID_TAG_TITLE = fields.ForeignKey(
        'data_records.ProvenanceSystemFunctionDataRecordsTagTitle', verbose_name='主题',
        on_delete=models.CASCADE, null=False, blank=False, to_field='ID', clearable=True, placeholder='主题', )
    ID_TAG = fields.ForeignKey(
        'data_records.ProvenanceSystemFunctionDataRecordsTag', verbose_name='标签',
        on_delete=models.CASCADE, null=False, blank=False, to_field='ID', clearable=True, placeholder='标签', )

    class Meta:
        db_table = "ProvenanceSystemFunctionDataRecordsTagTitleTag"
        ordering = ['-CREATE_TIME']
        verbose_name = "主题关联标签"
        verbose_name_plural = verbose_name
        unique_together = ('ID_TAG_TITLE', 'ID_TAG',)

    def __str__(self):
        return f'{self.ID_TAG_TITLE}:{self.ID_TAG}'


# 文件对象标签
class ProvenanceSystemFunctionDataRecordsFileObjectTag(BasesModelCommunalId):
    """文件对象标签"""
    ID_TAG = fields.ForeignKey(
        'data_records.ProvenanceSystemFunctionDataRecordsTag', verbose_name='标签', on_delete=models.CASCADE,
        null=True, blank=True, to_field='ID', clearable=True, placeholder='标签', )
    ID_FILE_OBJECT = fields.ForeignKey(
        'data_records.ProvenanceSystemFunctionDataRecordsSystemFileObject', verbose_name='文件对象',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='文件对象', )

    class Meta:
        db_table = "ProvenanceSystemFunctionDataRecordsFileObjectTag"
        ordering = ['-CREATE_TIME']
        verbose_name = "文件对象标签"
        verbose_name_plural = verbose_name
        unique_together = ('ID_TAG', 'ID_FILE_OBJECT',)

    def __str__(self):
        return f'{self.ID_TAG}:{self.ID_FILE_OBJECT}'
