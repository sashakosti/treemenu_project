from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='treeapp_home'),
    path('about/', views.about, name='treeapp_about'),
    path('contact/', views.contact, name='treeapp_contact'),
    path('menu/', views.menu, name='treeapp_menu'),
    path('main_menu/', views.main_menu_view, name='treeapp_main_menu'),
    path('help/', views.help, name='treeapp_help'),
    path('about/news/', views.news_view, name='news'),
]