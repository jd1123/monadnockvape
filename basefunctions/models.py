from django.db import models
from django.contrib import admin

# Create your models here.
class IndexImage(models.Model):
    image_name = models.CharField(max_length = 40)
    image = models.ImageField(upload_to = "static/user_data/")
    image_hires = models.ImageField(upload_to = "static/user_data/")
    title = models.CharField(max_length = 140)
    caption = models.CharField(max_length = 140)

    def __unicode__(self):
        return self.image_name

class IndexImageAdmin(admin.ModelAdmin):
    list_display = ['image_name', 'title', 'caption']


class IndexMosiac(models.Model):
    mosiac_name = models.CharField(max_length = 50, default="frontpage_mosiac")
    image1 = models.ForeignKey(IndexImage, related_name='image1')
    image2 = models.ForeignKey(IndexImage, related_name='image2')
    image3 = models.ForeignKey(IndexImage, related_name='image3')
    image4 = models.ForeignKey(IndexImage, related_name='image4')
    image5 = models.ForeignKey(IndexImage, related_name='image5')
    image6 = models.ForeignKey(IndexImage, related_name='image6')
    image7 = models.ForeignKey(IndexImage, related_name='image7')
    image8 = models.ForeignKey(IndexImage, related_name='image8')
    image9 = models.ForeignKey(IndexImage, related_name='image9')

    def __unicode__(self):
        return "IndexMosiac"

class IndexMosiacAdmin(admin.ModelAdmin):
    list_display = ['mosiac_name']
