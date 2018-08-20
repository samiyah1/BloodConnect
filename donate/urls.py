from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'signup/donor/',views.donorsignup, name = 'donor-signup'),
    url(r'signup/bank/',views.banksignup, name = 'bank-signup'),
]
