from django.db import models
from django.urls import reverse

class Product(models.Model):
	CHOICE_PRODUCT = (
		('vegetable', 'овочі'),
		('fruit', 'фрукти та ягоди'),
		("meat", "м'ясо"),
		('seafood', 'морепродукти'),
		('eggs', 'яйця'),
		('milk', 'молочні продукти'),
		('cereals', 'крупи'),
		('water', 'вода'),

	)
	product_name = models.CharField(max_length=150, verbose_name="Назва продукту", unique=True)
	categori_product = models.CharField(max_length=150, verbose_name="Категорія продукту", null=False, choices=CHOICE_PRODUCT)
	protein = models.FloatField(verbose_name="Білки")
	fat = models.FloatField(verbose_name="Жири")
	carbohydrat = models.FloatField(verbose_name="Вугливоди")
	kll = models.FloatField(verbose_name="Калорійність")
	slug = models.SlugField(editable=False)

	def __str__(self):
		return self.product_name

	def get_product_slug(self):
		return reverse('product_detail', kwargs={'product_slug': self.slug})

	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукти'

class Dish(models.Model):
	dish_name = models.CharField(max_length=30, verbose_name="Назва страви", unique=True)
	product = models.ManyToManyField(Product, blank=True, verbose_name="Назва продукту")
	caunt = models.IntegerField(null=False, verbose_name="Кількість продуктів")
	slug = models.SlugField(editable=False)
	weist_dish = models.FloatField(verbose_name="Вага страви")
	total_dish_kll = models.FloatField(verbose_name="Калорійність страви")

	# def __str__(self):
	# 	return "Продукт додано у страву {0}".format(self.product.product_name)

	def get_dish_slug(self):
		return reverse('dish_detail', kwargs={'dish_slug': self.slug})

	def get_products(self):
		return "\n".join([p.product_name for p in self.product.all()])

	class Meta:
		verbose_name = 'Страва'
		verbose_name_plural = 'Страви'

class Menu(models.Model):
	dish = models.ForeignKey(Dish, verbose_name="Назва страви", on_delete=models.CASCADE, null=True, blank=True)
	total_kll = models.FloatField(verbose_name="Загальна калорійність меню")

	def __str__(self):
		return "Страву додано у меню {0}".format(self.dish)

	def add_dish_to_menu(self, product_slug):
		menu = self
		product = Product.objects.get(slug=product_slug)
		new_dish, _ = Dish.objects.get_or_create(product=product, count=product.product_name)
		if new_dish not in menu.dish.all():
			menu.dish.add(new_dish)
			menu.save()

	def remove_dish_from_menu(self, prod_slug):
		menu = self
		prod = Product.objects.get(slug=prod_slug)
		for menu_dish in menu.dish.all():
			if menu_dish.product == prod:
				menu.dish.remove(menu_dish)
				menu.save()

	def get_dish_name(self):
		return "\n".join([d.dish_name for d in self.dish.all()])

	class Meta:
		verbose_name = 'Меню'
		verbose_name_plural = 'Меню'

class Person(models.Model):
	CHOICE_GENDER = (
		('male', 'Чол.'),
		('female', 'Жін.'),
		)

	CHOICE_GROUP_WORK = (
		('the_first', 'перша'),
		('the_second', 'друга'),
		('the_third', 'третя'),
		)

	person_name = models.CharField(verbose_name="Ім'я користувача", max_length=50, unique=True)
	person_birthday = models.DateField(verbose_name="День народження", max_length=8)
	person_gender = models.CharField(verbose_name="Стать", max_length=150, choices=CHOICE_GENDER)
	person_work_group = models.CharField(verbose_name="Робоча група", max_length=150, choices=CHOICE_GROUP_WORK)

	def __str__(self):
		return self.person_name

	class Meta:
		verbose_name = 'Користувач'
		verbose_name_plural = 'Користувачі'

class Work_Group(models.Model):
	number_group = models.OneToOneField(Person, on_delete=models.CASCADE, verbose_name="Робоча група")
	age = models.DateField(verbose_name="Вік", max_length=8)
	energy = models.FloatField(verbose_name="Енергія")

	def __str__(self):
		return self.number_group

	class Meta:
		verbose_name = 'Робоча група'
		verbose_name_plural = 'Робоча група'