from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.person_list, name='people'),
    url(r'^sort/$', views.sort, name='sort'),
    url(r'^search/$', views.search, name='search'),
    url(r'^detail/$', views.person, name='person'),
    url(r'^random/$', views.person_random, name='random')
]