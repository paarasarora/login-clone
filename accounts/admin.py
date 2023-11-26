from django.contrib import admin
from .models import *
# Register your models here.
class UserAdminModel(admin.ModelAdmin):
    list_display = ('username',)
    search_fields=('username',)

admin.site.register(User,UserAdminModel)