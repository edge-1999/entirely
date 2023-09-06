import copy
import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, reverse

from docs.utils.response_communal.return_format_communal import JsonResponsePostJsonBasic
from menu_management.result import MenuSonManagement


def get_son_menus(request):
    """
    获取菜单
    :param request:
    :type request:
    :return:
    :rtype:
    """
    return_json_data = JsonResponsePostJsonBasic()
    if request.method.upper() == "POST":
        menu_id = request.POST.get('menu_id')
        if menu_id:
            son_menu = MenuSonManagement(menu_id, ['18', '16', '17'])
            son_menus = son_menu.def_run_son_menu_message()
            if son_menu.display:
                return_json_data.data = son_menus
                del son_menus
                return_json_data.appCode = 200
                return_json_data.appMessage = 'ok'
                return_json_data.expandKeys = None
                return_json_data.success = True
                return_json_data.menu_id = menu_id
            # return render(request, 'cornerstone.html', context={'data': return_json_data.dict})
        # return JsonResponse(data={'error_data': '监测到异常，已报警处理！'})
    data = return_json_data.dict
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json")
