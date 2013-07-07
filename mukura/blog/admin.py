'''
Created on 06-Jul-2013

@author: srihari
'''

from django.contrib import admin
from models import Post, PostCategory

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'time_stamp')
    list_filter = ('published', 'categories')
    search_fields = ('title',)
    save_as = True
#    date_hierarchy = 'time_stamp'
    
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'ordering')
    list_filter = ('active',)
    search_fields = ('title',)
    list_editable = ('ordering',)    
    
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
