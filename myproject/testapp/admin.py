from django.contrib import admin
from .models import Task, Client

class TaskAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'author')
    list_filter = ("pub_date", 'author')
    search_fields = ("text",)
    empty_value_display = "-пусто-"

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')
    search_fields = ("name",)
    empty_value_display = "-пусто-"

admin.site.register(Task, TaskAdmin)
admin.site.register(Client, ClientAdmin)