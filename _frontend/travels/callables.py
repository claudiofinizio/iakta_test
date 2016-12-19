# Project imports
# from _frontend.settings import BASE_DIR
from . import json_query


# Project constants
IAKTA_BASE_URL = 'http://www.iakta.it:3000'
TRAVELLER = 'travelog'
POINTS = 'points'
POSTS = 'posts'

from pprint import pprint

def travelogs_all():
    requested_traveller_id = 1
    requested_url = '/'.join([
        IAKTA_BASE_URL,
        TRAVELLER,
        str(requested_traveller_id),
    ])
    data = json_query.decode_from_iakta_website(requested_url)
    return data['travelogs']
    
    
def travel_posts(travel_pk):
    requested_url = '/'.join([
        IAKTA_BASE_URL,
        POSTS,
        str(travel_pk),
    ])
    # Retrieve posts for a given travel
    data = json_query.decode_from_iakta_website(requested_url)
    return data['posts'] 
    
    
def travel_points(travel_pk):
    requested_url = '/'.join([
        IAKTA_BASE_URL,
        POINTS,
        str(travel_pk),
    ])
    data = json_query.decode_from_iakta_website(requested_url)
    
    pprint(data['points'])
    return data['points'] 

    
    
def filter_travelogs(travel_pk):
    travelogs = travelogs_all()
    return [
            travel for travel in travelogs if str(travel['id'])==str(travel_pk)
        ][0]
    
def map_center(point_list):
    pprint(point_list)
    latitude_list = [float(e['latitude']) for e in point_list]
    latitude_center = sum(latitude_list) / len(latitude_list)
    longitude_list = [float(e['longitude']) for e in point_list]
    longitude_center = sum(longitude_list) / len(longitude_list)
    return {
        'latitude_center': latitude_center,
        'longitude_center': longitude_center,
    }