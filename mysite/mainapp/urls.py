from django.urls import path
from django.conf.urls import include, url
from mainapp.models import Product, Dish, Menu, Person, Work_Group
from . import views
from django.conf import settings

urlpatterns = [
	url(r'^$', views.main_page, name='index'),
	url(r'^menu/$', views.menu_page, name='menu'),
	url(r'^menu/diet_menu/$', views.dietmenu_page, name='diet_menu'),
	url(r'^menu/menu_create/$', views.menucreate_page, name='menu_create'),
	url(r'^menu/calculate/$', views.calculate_page, name='calculate'),
	url(r'^kallori/$', views.kallori_page, name='kallori'),
	url(r'^kallori/kll_product$', views.kllproduct_page, name='kll_product'),
	url(r'^manual/$', views.manual_page, name='manual'),
	url(r'^sign_in/$', views.sign_in_page, name='sign_in'),
	url(r'^registration/$', views.registration_page, name='registration'),


	
	#path('', views.index, name = 'index'),
]