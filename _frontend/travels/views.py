# Python imports
import base64

# Django imports
from django.shortcuts import render
from django.http import Http404  

# Project imports
from . import callables


from pprint import pprint


# App views
def index(request):
    page = 'travels/index.html'
    context={}
    context = {
        'travelogs': callables.travelogs_all(),
    }
    return render(request, page, context)
    
    
def posts(request, travel_pk):
    if 233. < int(travel_pk) < 240.:
        page = 'travels/posts.html'
        context={}
        # Retrive info on the travel identified by pk in the signature 
        context['posts'] = callables.travel_posts(travel_pk)
        # Optionally, retrieve posts for a given travel
        context['travel'] = callables.filter_travelogs(travel_pk)
        # pprint(context['travel'])
    else:
        raise Http404 
    return render(request, page, context)
    
    
def points(request, travel_pk):
    page = 'travels/points.html'
    context={}
    # requested_url = '/'.join([
        # IAKTA_BASE_URL,
        # POINTS,
        # str(pk),
    # ])
    # data = json_query.decode_from_iakta_website(requested_url)
    
    # pprint(data['points'])
    context['points'] = callables.travel_points(travel_pk)
    # context['points'] = data['points']
    return render(request, page, context)
    
    
