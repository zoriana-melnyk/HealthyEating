from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# from .forms import UserForm

#from django.shortcuts import get_object_or_404

#from django.views.generic import View

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

def manual_page(request):
	return render(request, 'frontend/manual.html', {})

def sign_in_page(request):
	return render(request, 'frontend/sign_in.html', {})

def registration_page(request):
	if request.method == 'POST':
		form = RegisterationFrom(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('frontend/index.html')
		else:
			form = RegisterationFrom()
		return render(request, 'frontend/registration.html', {'form': form})
	# return render(request, 'frontend/registration.html', {})
 
# def forms(request):
#     userform = UserForm()
#     return render(request, "frontend/sign_in.html", {"form": userform})

	

#class HomePage(View):
	#def get(self, request, slug):
		#post = get_object_or_404()
		


