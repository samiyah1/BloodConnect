from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^index/', views.index, name='index'),
    url(r'^signup/donor/',views.donorsignup, name = 'donor-signup'),
    url(r'^signup/bank/',views.banksignup, name = 'bank-signup'),
    url(r'^showdonorprofile/(?P<user_id>\d+)',views.showdonorprofile, name='show-profile')
]
