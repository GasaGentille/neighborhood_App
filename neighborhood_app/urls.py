from django.conf.urls import url
from . import views


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^newbiz/',views.new_business,name = 'new-business'),
     url(r'^newevent/',views.new_events,name = 'new-event'),
    url(r'^neighborhood/(?P<neighborhood_id>\d+)',views.neighborhood,name = 'neighborhood'),
    url(r'^profile/',views.new_profile,name = 'profile'),
    url(r'^new/profile$', views.myprofile, name='profilee'),
]