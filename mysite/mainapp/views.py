from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .forms import CreateUserForm

#from django.contrib.auth.forms import UserCreationForm


from .models import Product, Dish, Menu, Person, Work_Group

def main_page(request):
	return render(request, 'frontend/index.html', {})

def menu_page(request):
	return render(request, 'frontend/menu.html', {})

def dietmenu_page(request):
	return render(request, 'frontend/diet_menu.html', {})

def sportmenu_page(request):
	return render(request, 'frontend/sport_menu.html', {})

def childrenmenu_page(request):
	return render(request, 'frontend/children_menu.html', {})

def menucreate_page(request):
	products = Product.objects.order_by('-id').values();
	context = {
		'products': list(products)
	}
	return render(request, 'frontend/menu_create.html', context)

def calculate_page(request):
	products = Product.objects.order_by('-id').values();
	context = {
		'products': list(products)
	}
	return render(request, 'frontend/calculate.html', context)

def kallori_page(request):
	return render(request, 'frontend/kallori.html', {})

def vegKll_page(request):
	return render(request, 'frontend/veg_kll.html', {})

def fruitKll_page(request):
	return render(request, 'frontend/fruit_kll.html', {})

def seafoodKll_page(request):
	return render(request, 'frontend/seafood_kll.html', {})

def meatKll_page(request):
	return render(request, 'frontend/meat_kll.html', {})

def kallReg_page(request):
	return render(request, 'frontend/kall_reg.html', {})

def vegForReg_page(request):
	return render(request, 'frontend/veg_for_reg.html', {})

def fruitForReg_page(request):
	return render(request, 'frontend/fruit_for_reg.html', {})

def seafoodForReg_page(request):
	return render(request, 'frontend/seafood_for_reg.html', {})

def meatForReg_page(request):
	return render(request, 'frontend/meat_for_reg.html', {})

def manual_page(request):
	return render(request, 'frontend/manual.html', {})

def manualReg_page(request):
	return render(request, 'frontend/manual_reg.html', {})

def sign_in_page(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Не правильний логін або пароль')

		context = {}
		return render(request, 'frontend/sign_in.html', context)

def log_out_page(request):
	logout(request)
	return redirect('sign_in')

def registration_page(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Акаунт був створений' + user)
				return redirect('sign_in')
		context = {'form': form}
		return render(request, 'frontend/registration.html', context)

def home_page(request):
	context = {}
	return render(request, 'frontend/home.html', context)


