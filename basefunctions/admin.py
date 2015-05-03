from django.contrib import admin
from basefunctions.models import IndexImage, IndexImageAdmin, IndexMosiac, IndexMosiacAdmin

# Register your models here.
admin.site.register(IndexImage, IndexImageAdmin)
admin.site.register(IndexMosiac, IndexMosiacAdmin)
