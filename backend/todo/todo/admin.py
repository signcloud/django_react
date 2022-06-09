from django.contrib import admin

# Register your views here.

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', "title", 'completed', 'user')
    list_display_links = ('id',)
    list_editable = ('title', 'user', 'completed',)


admin.site.register(Task, TaskAdmin)
