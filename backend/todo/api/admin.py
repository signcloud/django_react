from django.contrib import admin

# Register your models here.

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", 'completed', 'user')
    list_display_links = ('title',)
    list_editable = ('user', 'completed',)


admin.site.register(Task, TaskAdmin)
