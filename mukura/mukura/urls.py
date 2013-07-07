from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'mukura.views.home', name='home'),
     url(r'^about/?$', 'mukura.views.about', name='about'),
     url(r'^travel/?$', 'mukura.views.travel', name='travel'),
     url(r'^contact/?$', 'mukura.views.contact', name='contact'),
     url(r'^blog', include('blog.urls')),
     url(r'^inspire', include('inspire.urls')),
     url(r'^admin/', include(admin.site.urls)),
)
