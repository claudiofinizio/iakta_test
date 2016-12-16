from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^post/(?P<pk>\w+)$', views.posts, name='travel-posts'),
    url(r'^points/(?P<pk>\w+)$', views.points, name='travel-points'),
]


