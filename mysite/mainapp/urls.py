from django.urls import path
from django.conf.urls import include, url
from mainapp.models import Product, Dish, Menu, Person, Work_Group
from . import views
from django.conf import settings

urlpatterns = [
	url(r'^$', views.main_page, name='index'),
	url(r'^sign_in$', views.sign_in_page, name='sign_in'),
	url(r'^log_out/$', views.log_out_page, name='log_out'),
	url(r'^registration/$', views.registration_page, name='registration'),
	url(r'^home$', views.home_page, name='home'),
	url(r'^menu/$', views.menu_page, name='menu'),
	url(r'^menu/diet_menu/$', views.dietmenu_page, name='diet_menu'),
	url(r'^menu/sport_menu/$', views.sportmenu_page, name='sport_menu'),
	url(r'^menu/children_menu/$', views.childrenmenu_page, name='children_menu'),
	url(r'^menu/menu_create/$', views.menucreate_page, name='menu_create'),
	url(r'^menu/calculate/$', views.calculate_page, name='calculate'),
	url(r'^kallori/$', views.kallori_page, name='kallori'),
	url(r'^kallori/veg_kll$', views.vegKll_page, name='veg_kll'),
	url(r'^kallori/fruit_kll$', views.fruitKll_page, name='fruit_kll'),
	url(r'^kallori/seafood_kll$', views.seafoodKll_page, name='seafood_kll'),
	url(r'^kallori/meat_kll$', views.meatKll_page, name='meat_kll'),
	url(r'^kall_reg/$', views.kallReg_page, name='kall_reg'),
	url(r'^kall_reg/veg_for_reg$', views.vegForReg_page, name='veg_for_reg'),
	url(r'^kall_reg/fruit_for_reg$', views.fruitForReg_page, name='fruit_for_reg'),
	url(r'^kall_reg/seafood_for_reg$', views.seafoodForReg_page, name='seafood_for_reg'),
	url(r'^kall_reg/meat_for_reg$', views.meatForReg_page, name='meat_for_reg'),
	url(r'^manual/$', views.manual_page, name='manual'),
	url(r'^manual_reg/$', views.manualReg_page, name='manual_reg'),

	#path('', views.index, name = 'index'),
]