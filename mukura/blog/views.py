'''
Created on 06-Jul-2013

@author: srihari
'''

from django.shortcuts import render_to_response
from models import PostCategory, Post
from django.template.context import RequestContext
from django.http import Http404

def post_list(request, cat_slug=None):
    is_home = not bool(cat_slug)
    selected_category = None
    category_list = [(cat.title, cat.get_absolute_url()) for cat in PostCategory.objects.filter(active=True)]
    post_list = Post.objects.filter(published=True).order_by("-time_stamp")
    if  cat_slug:
        post_list = post_list.filter(categories__slug=cat_slug)
        selected_category = PostCategory.objects.get(slug=cat_slug).title
    return render_to_response("post_list.html", RequestContext(request, {'is_home': is_home, 
                                                                         'category_list': category_list, 'post_list':post_list,
                                                                         'selected_category': selected_category,}))
    
def post_detail(request, post_slug):
    print "---post---slug:" + post_slug
    if not post_slug:
        return Http404
    try:
        post = Post.objects.get(slug=post_slug)
        return render_to_response("post_detail.html", RequestContext(request, {"post": post}))
    except:
        raise Http404

    
    
    