from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^index/', views.index, name='index'),
    url(r'^index/(?P<user_id>\d+)', views.index, name='show-profile'),
    url(r'^signup/donor/',views.donorsignup, name = 'donor-signup'),
    url(r'^signup/bank/', views.banksignup, name='bank-signup'),
    url(r'^post/drive/', views.donation, name='donation'),
]
