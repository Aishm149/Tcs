from django.conf.urls import url
from . import views
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views as core_views

urlpatterns = [
#   url(r'^$', views.login_list, name='login_list'),
#     url(r'^$', views.edu_new, name='edu_new'),
#
#     url(r'^company/$', views.company_new, name='company_new'),
# url(r'^$', core_views.home, name='home'),
#     url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
#     url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
#     url(r'^signup/$', core_views.signup, name='signup'),
]