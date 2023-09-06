from django.urls import path, register_converter

from docs.utils.urls_communal.url_converters import MenuId
from .views.home_page import home
from .views.view_menu import get_son_menus
from .views.menu_test import test
from .views.view_system import get_system

app_name = "menu_management"

register_converter(MenuId, 'menu_id')

urlpatterns = [
    path('', home, name='HomePage'),
    # path('menu', get_son_menus, name='Menu'),
    # path('menu/<str:menu_id>', get_son_menus, name='menu_son'),
    path('Test', test, name='Test'),
    path('GetMenuSonModel', get_son_menus, name='GetMenuSonModel'),
    path('GetSystemnModel', get_system, name='GetSystemnModel'),
]
