from django.contrib import admin

from .models import Product, Dish, Menu, Person, Work_Group

#admin.site.register(Dish)
#admin.site.register(Person)

class ProductAdmin(admin.ModelAdmin):
	list_display = ('product_name', 'protein', 'fat', 'carbohydrat', 'kll',)
	list_filter = ('categori_product',)

admin.site.register(Product, ProductAdmin)

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
	list_display = ('product', 'caunt',)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
	list_display = ('get_products', 'total_kll',)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	list_display = ('person_name', 'person_birthday', 'person_gender',)

@admin.register(Work_Group)
class Work_GroupAdmin(admin.ModelAdmin):
	list_display = ('number_group', 'age', 'energy',)