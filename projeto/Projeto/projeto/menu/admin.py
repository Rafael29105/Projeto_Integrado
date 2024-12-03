from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')  
    list_display_links = ('name',)  
    list_filter = ('price',)
    search_fields = ('name', 'description')
    actions = ['delete_selected']
admin.site.register(MenuItem, MenuItemAdmin)
