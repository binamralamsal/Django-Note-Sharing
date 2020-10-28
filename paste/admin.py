from django.contrib import admin
from . import models
from django.contrib import admin


class TextFileAdmin(admin.ModelAdmin):
    list_display = ['text', 'author', 'date']
    search_fields = ['text', 'author']


admin.site.register(models.TextFile, TextFileAdmin)
