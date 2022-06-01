from django.contrib import admin
from .models import Category, Diseases, Doctors, News

class CategoryAdmin(admin.ModelAdmin):
    exclude = ['slug', 'created_at']


class DiseasesAdmin(admin.ModelAdmin):
    exclude = ['slug']


class DoctorsAdmin(admin.ModelAdmin):
    exclude = ['slug',]

class NewsAdmin(admin.ModelAdmin):
    exclude = ['slug','date']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Diseases, DiseasesAdmin)
admin.site.register(Doctors, DoctorsAdmin)
admin.site.register(News,NewsAdmin)
