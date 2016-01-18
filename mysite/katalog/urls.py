from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tovar_list, name='tovar_list'),
]
