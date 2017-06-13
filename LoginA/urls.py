from django.conf.urls import url
from . import views


urlpatterns = [
#   url(r'^$', views.login_list, name='login_list'),
    url(r'^$', views.profile_new, name='profile_new'),
]