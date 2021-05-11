from django.contrib import admin
from .models import catagories, show, watch_history


@admin.register(show)
class shows(admin.ModelAdmin):
    list_display = ['show_name','show_title']
    list_display_links = ['show_name','show_title']

@admin.register(catagories)
class catagories(admin.ModelAdmin):
    pass

admin.site.register(watch_history)