from django.contrib import admin
from inventory.models import *

# Register your models here.

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(InvItem, InvItemAdmin)
