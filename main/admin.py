from django.contrib import admin
from .models import ToDoList, Item, Folder
from mptt.admin import MPTTModelAdmin

# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Item)
admin.site.register(Folder, MPTTModelAdmin)