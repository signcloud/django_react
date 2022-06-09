from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', "email", 'first_name', 'last_name')
    list_display_links = ('id',)
    list_editable = ("email", 'first_name', 'last_name')


admin.site.register(User, UserAdmin)
# Register your views here.
