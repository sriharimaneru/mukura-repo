'''
Created on 06-Jul-2013

@author: srihari
'''

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
     url(r'^/?$', 'blog.views.post_list', name='post_list'),
     url(r'^/categories/(?P<cat_slug>.*[^/])/?$', 'blog.views.post_list', name='post_list'),
     url(r'^/(?P<post_slug>.*[^/])/?$', 'blog.views.post_detail', name='post_detail'),
)
