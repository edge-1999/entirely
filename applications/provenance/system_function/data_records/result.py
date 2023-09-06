import os

from data_records.models import (
    ProvenanceSystemFunctionDataRecordsSystem,
    ProvenanceSystemFunctionDataRecordsSystemFolder, ProvenanceSystemFunctionDataRecordsTag,
    ProvenanceSystemFunctionDataRecordsSystemFileObject, ProvenanceSystemFunctionDataRecordsFileObjectTag
)


class AuthorSystemMessages(object):
    """获取账户所有记录系统信息"""

    def __init__(self, subscriber_id):
        self.subscriber_id = subscriber_id
        self.display = False
        self.data = []

    def def_get_system_messages(self):
        self.display = False
        self.data.clear()
        if self.subscriber_id:
            systems = ProvenanceSystemFunctionDataRecordsSystem.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_SUBSCRIBER=self.subscriber_id,
            ).values('ID', 'ID_UNIQUE', "SYSTEM_CATEGORY__ABBREVIATION", "NAME")
            if systems.exists():
                for system in systems:
                    return_data_list = {
                        "ID_SYSTEM": system.get('ID').hex,
                        "SYSTEM_UNIQUE": system.get('ID_UNIQUE'),
                        "SYSTEM_NAME": system.get('NAME'),
                        "SYSTEM_CATEGORY": system.get('SYSTEM_CATEGORY__ABBREVIATION'),
                    }
                    self.data.append(return_data_list)
            self.display = True


class AuthorSystemFolderMessages(object):
    """获取账户指定系统下的所有工作目录"""

    def __init__(self, system_id):
        self.system_id = system_id
        self.display = False
        self.data = []

    def def_get_folder_messages(self):
        """返回查询系统下所有的目录信息"""
        self.display = False
        self.data.clear()
        if self.system_id:
            folders = ProvenanceSystemFunctionDataRecordsSystemFolder.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_SYSTEM=self.system_id,
            ).values('ID', 'INODE', "NAME", "PATH")
            if folders.exists():
                for folder in folders:
                    return_data_list = {
                        "ID_FOLDER": folder.get('ID').hex,
                        "FOLDER_INODE": folder.get('INODE'),
                        "FOLDER_NAME": folder.get('NAME'),
                        "FOLDER_CATEGORY": folder.get('PATH'),
                        "FOLDER_DISPLAY": self.__def_get_folder_determine_metadata_messages(folder.get('ID').hex),
                    }
                    self.data.append(return_data_list)

            self.display = True

    def __def_get_folder_determine_metadata_messages(self, folder_id) -> bool:
        """返回目录的元信息"""
        self.display = False
        if folder_id:
            folder_message = ProvenanceSystemFunctionDataRecordsSystemFolder.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID=folder_id,
            ).values('INODE', "PATH")
            if folder_message.exists():
                folder_message = folder_message.first()
                folder_path = folder_message.get('PATH')
                if folder_path:
                    folder_inode = str(folder_message.get('INODE'))
                    inode = str(os.stat(folder_path).st_ino)
                    if folder_inode:
                        if inode == folder_inode:
                            self.display = True
        return self.display

    def gef_update_folder_metadata_messages(self, folder_id, update_data) -> bool:
        self.display = False
        if self.system_id:
            folder_message = ProvenanceSystemFunctionDataRecordsSystemFolder.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID=folder_id,
            ).values('INODE', "NAME", "PATH")
            if folder_message.exists():
                # folder_message = folder_message.first()
                update_data_path = update_data.get('PATH')
                if update_data_path:
                    inode = os.stat(update_data_path).st_ino
                    # ProvenanceSystemFunctionDataRecordsSystemFolder.objects.filter(
                    #     STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID=folder_id,
                    # ).update(PATH=update_data_path, INODE=inode)
                    folder_message.update(PATH=update_data_path, INODE=inode)
                update_data_name = update_data.get('NAME')
                if update_data_name:
                    # ProvenanceSystemFunctionDataRecordsSystemFolder.objects.filter(
                    #     STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID=folder_id,
                    # ).update(NAME=update_data_name)
                    folder_message.update(NAME=update_data_name)
                folder_message.save()
                self.display = True
        return self.display


class AuthorSystemFolderTagMessages(object):
    """获取账户指定系统下单个工作目录的标签"""

    def __init__(self, folder_id):
        self.folder_id = folder_id
        self.display = False
        self.data = []

    def def_get_tag_messages(self):
        self.display = False
        self.data.clear()
        if self.folder_id:
            tags = ProvenanceSystemFunctionDataRecordsTag.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_FOLDER=self.folder_id,
            ).values('ID', "NAME", )
            if tags.exists():
                for tag in tags:
                    return_data_list = {
                        "ID_TAG": tag.get('ID'),
                        "TAG_NAME": tag.get('NAME'),
                    }
                    self.data.append(return_data_list)
            self.display = True


class AuthorSystemFolderTagFileObjectMessages(object):
    """获取目录标签下文件对象"""

    def __init__(self, tags_id):
        """

        :param tags_id:
        :type tags_id: set
        :return:
        :rtype:
        """
        self.tags_id = list(tags_id)
        self.display = False
        self.data = []

    def def_get_file_object(self):
        """获取标签下所有的文件对象"""
        self.display = False
        self.data.clear()
        if self.tags_id:
            file_objects = ProvenanceSystemFunctionDataRecordsFileObjectTag.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_TAG__in=self.tags_id,
            ).values('ID_FILE_OBJECT', )
            if file_objects.exists():
                for file_object in file_objects:
                    return_data_list = {
                        "ID_FILE_OBJECT": file_object.get('ID_FILE_OBJECT'),
                    }
                    self.data.append(return_data_list)
            self.display = True


class AuthorSystemFileObjectMessages(object):
    """获取指定工作目录下所有的文件对象、或更新"""

    def __init__(self, folder_id):
        self.folder_id = folder_id
        self.display = False
        self.data = []

    def del_def_get_file_object_messages(self):
        """获取当前目录下的所有文件对象"""
        self.display = False
        self.data.clear()
        if self.folder_id:
            folders = ProvenanceSystemFunctionDataRecordsSystemFileObject.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_FOLDER=self.folder_id,
                ID_ORGANIZATIONS__STATUS_IS_DELETE='0', ID_ORGANIZATIONS__STATUS_IS_EFFECTIVE=1,
            ).values('INODE', "NAME", "PATH", "TYPE__ABBREVIATION", )
            if folders.exists():
                for folder in folders:
                    return_data_list = {
                        "ID_FILE_OBJECT": folder.get('INODE'),
                        "FILE_OBJECT_NAME": folder.get('NAME'),
                        "FILE_OBJECT_PATH": folder.get('PATH'),
                        "FILE_OBJECT_TYPE": folder.get('TYPE__ABBREVIATION'),
                    }
                    self.data.append(return_data_list)
            self.display = True

    def def_get_file_object_init(self):
        """初始化当前目录下的所有文件对象"""
        self.display = False
        self.data.clear()
        if self.folder_id:
            for root, dirs, files in os.walk(self.folder_id):
                if files:
                    for file_name in files:
                        file_path_q = os.path.join(root, file_name)
                        file_data = self.def_get_file_inode(file_path_q)
                        inode = file_data

                if dirs:
                    for dir_name in dirs:
                        folder_path_q = os.path.join(root, dir_name)
                        folder_data = self.def_get_file_inode(folder_path_q)
                        inode = folder_data

    def def_get_file_inode(self, file_path):
        """获取文件元信息"""
        self.display = False
        file_stat = os.stat(file_path)
        inode = file_stat.st_ino
        self.display = True
        return inode
