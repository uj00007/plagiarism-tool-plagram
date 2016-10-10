
from django.conf.urls import url
from django.contrib import admin
from signup import views

app_name = 'signup'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^success/$',views.success,name='success'),
    url(r'^loginsuccess/$',views.loginsuccess,name='loginsuccess')
]
