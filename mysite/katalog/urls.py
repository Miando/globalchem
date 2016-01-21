from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^moloko/$', views.moloko_list, name='moloko_list'),
    url(r'^pivo/$', views.pivo_list, name='pivo_list'),
    url(r'^myaso/$', views.myaso_list, name='myaso_list'),
    url(r'^gigiena/$', views.gigiena_list, name='gigiena_list'),
    url(r'^zasib/(?P<pk>[0-9]+)/$', views.tovar_detail, name='tovar_detail'),
]
