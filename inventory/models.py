from django.db import models
from django.contrib import admin
# from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.TextField(max_length = 200)
    picture_url = models.URLField(blank=True)
    def __unicode__(self):
        return self.category_name

class SubCategory(models.Model):
    category = models.ForeignKey(Category)
    sub_category_name = models.TextField(max_length = 200)
    picture_url = models.URLField(blank=True)
    def __unicode__(self):
        return self.sub_category_name

class InvItem(models.Model):
    category = models.ForeignKey(Category)
    sub_category = models.ForeignKey(SubCategory, blank=True)
    item_name = models.TextField(max_length = 200)
    description = models.TextField(max_length = 1000, blank=True)
    date_added = models.DateField(blank=True)
    price = models.FloatField(blank=True)
    sku = models.TextField(max_length=8, blank=True)
    # which to use???
    picture_url = models.URLField(blank=True)
    # img = models.ImageField(upload_to = 'static/img')

    def __unicode__(self):
        return self.item_name

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name','picture_url']
    search_fields = ['category_name']

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['category' , 'sub_category_name','picture_url']
    search_fields = ['category', 'sub_category_name']

class InvItemAdmin(admin.ModelAdmin):
    list_display = ['category', 'sub_category', 'item_name', 'date_added', 'price', 'sku']
    search_fields = ['category', 'sub_category', 'item_name', 'date_added', 'price']
