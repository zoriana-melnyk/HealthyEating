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

def menucreate_page(request):
	return render(request, 'frontend/menu_create.html', {})

def calculate_page(request):
	products = Product.objects.order_by('-id').values();
	context = {
		'products': list(products)
	}
	return render(request, 'frontend/calculate.html', context)

def kallori_page(request):
	return render(request, 'frontend/kallori.html', {})

def kllproduct_page(request):
	return render(request, 'frontend/kll_product.html', {})

def kallReg_page(request):
	return render(request, 'frontend/kall_reg.html', {})

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
	# return render(request, 'frontend/registration.html', {})

def home_page(request):
	context = {}
	return render(request, 'frontend/home.html', context)


