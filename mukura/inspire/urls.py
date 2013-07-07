'''
Created on 06-Jul-2013

@author: srihari
'''

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
     url(r'^/?$', 'inspire.views.inspire_list', name='inspire_list_home'),
     url(r'^/categories/(?P<cat_slug>.*[^/])/?$', 'inspire.views.inspire_list', name='inpsire_list'),
     url(r'^/(?P<inspire_profile_slug>.*[^/])/?$', 'inspire.views.inspire_profile', name='inpsire_profile'),
)
