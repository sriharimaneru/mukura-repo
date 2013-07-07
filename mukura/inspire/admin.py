'''
Created on 06-Jul-2013

@author: srihari
'''


from django.contrib import admin
from models import InspireCategory, InspireProfile

class InspireProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'published', 'time_stamp')
    list_filter = ('published', 'categories')
    search_fields = ('name',)
    filter_horizontal = ('categories', 'posts',)
    
    class Media:
        css = {
               'all': ('/static/admin/js/jquery.min.js', '/static/admin/js/jquery.init.js',)
               }
    
class InspireCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'ordering', 'category_type')
    list_filter = ('active', 'category_type')
    search_fields = ('title',)
    list_editable = ('ordering',)    
    
admin.site.register(InspireProfile, InspireProfileAdmin)
admin.site.register(InspireCategory, InspireCategoryAdmin)
