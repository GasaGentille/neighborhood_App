from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url('^$',views.project,name = 'project'),
    url(r'^profile',views.profile, name='profile'),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^add/profile$', views.add_profile, name='add_profile'),
    url(r'^edit/profile$', views.update_profile, name='edit_profile'),
    url(r'^search/', views.search_results, name='search_results'),
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)