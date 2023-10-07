from django.contrib import admin
from . import models

class NewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'link')
    list_display_links = ('id', 'title', 'link')

admin.site.register(models.New, NewAdmin)
