import copy
import json
import os

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, reverse

from data_records.result import AuthorSystemMessages, AuthorSystemFolderMessages
from docs.utils.response_communal.return_format_communal import JsonResponsePostJsonBasic
from menu_management.result import MenuSonManagement


def test(request):
    """
    获取菜单
    :param request:
    :type request:
    :return:
    :rtype:
    """
    return_json_data = JsonResponsePostJsonBasic()
    if request.method.upper() == "GET":
        # subscriber_id = 'dc2c1d98b9604f87a383f3e522ef53e2'
        subscriber_id = 'a3a0cedfa6c04321986f71443f86b0f3'
        system_id = "4416b007659c458f9cd21c6a7e61ee2e"
        folder_id = "a8ed5a19635d4293b73c4a2f58c5f202"
        # a = AuthorSystemFolderMessages(system_id)
        # a.def_get_folder_messages()
        # a.gef_update_folder_metadata_messages(folder_id, {"NAME": "li"})
        # file_path_q = '/Volumes/LaCie/MyWork/Pcitc'
        file_path_q = '/Users/li/Library/Mobile Documents/com~apple~CloudDocs/program'
        file_stat = os.stat(file_path_q)
        inode = file_stat.st_ino
        return_json_data.inode = inode

        # if a.display:
        #     return_json_data.data = a.data
        #     return_json_data.appCode = 200
        #     return_json_data.appMessage = 'ok'
        #     return_json_data.expandKeys = None
        #     return_json_data.success = True
        #     del a
        # return_json_data.subscriber_id = subscriber_id
    data = return_json_data.dict
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json")
