'''
Created on 06-Jul-2013

@author: srihari
'''

from django.shortcuts import render_to_response
from models import InspireCategory, InspireProfile, RELATION, FIELD
from django.template.context import RequestContext
from django.http import Http404

def inspire_list(request, cat_slug=None):
    is_home = not bool(cat_slug)
    category_relation_list = [(cat.title, cat.get_absolute_url())
                               for cat in InspireCategory.objects.filter(active=True, category_type=RELATION)]
    category_field_list= [(cat.title, cat.get_absolute_url())
                              for cat in InspireCategory.objects.filter(active=True, category_type=FIELD)]
    profile_list = InspireProfile.objects.filter(published=True)
    if  cat_slug:
        profile_list = profile_list.filter(categories__slug=cat_slug)
    return render_to_response("inspire_list.html", RequestContext(request, 
                            {'is_home': is_home, 'category_relation_list': category_relation_list,
                              'category_field_list': category_field_list, 'profile_list': profile_list}))
    
def inspire_profile(request, inspire_profile_slug=None):
    if not inspire_profile_slug:
        return Http404
    try:
        profile = InspireProfile.objects.get(slug=inspire_profile_slug)
#        import pdb; pdb.set_trace()
        return render_to_response("inspire_profile.html", 
                                  RequestContext(request, {"profile": profile, "post_list": profile.posts.all()}))
    except:
        return Http404

    
    
    