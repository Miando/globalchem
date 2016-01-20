from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tovar_list, name='tovar_list'),
    url(r'^zasib/(?P<pk>[0-9]+)/$', views.tovar_detail, name='tovar_detail'),
]
