from django.db import models
from django.contrib import admin

# Create your models here.
class IndexImage(models.Model):
    image = models.ImageField(upload_to = "static/img/")
    caption = models.CharField(max_length = 40)

class IndexImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'caption']


class IndexMosiac(models.Model):
    image1 = models.ForeignKey(IndexImage)

class IndexMosiacAdmin(admin.ModelAdmin):
    list_display = ['image1']
