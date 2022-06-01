from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length = 100, blank = False, null = False, verbose_name = 'Kategoriya nomi')
	image = models.ImageField(upload_to = 'static/img')
	created = models.DateTimeField(auto_now = True)
	slug = models.SlugField()


	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		return super().save(*args, **kwargs)

	def __str__(self):
		return self.name
		

class Diseases(models.Model):
	name = models.CharField(max_length = 100, null = False, blank=False)
	image = models.ImageField(upload_to='static/img')
	description = models.TextField()
	price = models.IntegerField()
	parent = models.ForeignKey(Category, on_delete=models.CASCADE)
	slug = models.SlugField()


	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		return super().save(*args, **kwargs)

	def __str__(self):
		return self.name


class Doctors(models.Model):
	fullname = models.CharField(max_length = 100, null= False, blank = False)
	image = models.ImageField(upload_to = 'static/img')
	description = models.TextField()
	role = models.ForeignKey(Category, on_delete = models.CASCADE)
	number = models.CharField(max_length=20)
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.fullname)
		return super().save(*args, **kwargs)

	def __str__(self):
		return self.fullname


class News(models.Model):
	image = models.ImageField(upload_to = 'static/img')
	title = models.CharField(max_length = 120)
	description = models.DateField(auto_now= True)
	slug = models.SlugField()


	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		return super().save(*args, **kwargs)

	def __str__(self):
		return self.title
		

