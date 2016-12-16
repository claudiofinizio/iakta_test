# Python imports
import base64

# Django imports
from django.shortcuts import render

# Project imports
from _frontend.settings import BASE_DIR
from . import json_query


# Project constants
IAKTA_BASE_URL = 'http://www.iakta.it:3000'
TRAVELLER = 'travelog'
POINTS = 'points'
POSTS = 'posts'


from pprint import pprint

# App views
def index(request):
    page = 'travels/index.html'
    context={}
    requested_traveller_id = 1
    requested_url = '/'.join([
        IAKTA_BASE_URL,
        TRAVELLER,
        str(requested_traveller_id),
    ])
    data = json_query.decode_from_iakta_website(requested_url)
    pprint(data['travelogs'])
    
    context['travelogs'] = data['travelogs']
    return render(request, page, context)
    
    
def posts(request, pk):
    page = 'travels/posts.html'
    context={}
    requested_url = '/'.join([
        IAKTA_BASE_URL,
        POSTS,
        str(pk),
    ])
    data = json_query.decode_from_iakta_website(requested_url)
    pprint(data['posts'])
    
    context['posts'] = data['posts']
    return render(request, page, context)
    
    
def points(request, pk):
    page = 'travels/points.html'
    context={}
    requested_url = '/'.join([
        IAKTA_BASE_URL,
        POINTS,
        str(pk),
    ])
    data = json_query.decode_from_iakta_website(requested_url)
    
    pprint(data['points'])
    
    context['points'] = data['points']
    return render(request, page, context)
    
    
