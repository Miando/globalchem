from django.conf.urls import include, url
from django.contrib import admin
from katalog import views

urlpatterns = [
    url(r'^produkcia/', include('katalog.urls')),
    url(r'^produkcia/$',  views.produkcia, name='produkcia'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sertifikati/$', views.sertifikati, name='sertifikati'),
    url(r'^pro_nas/$', views.pro_nas, name='pro_nas'),
    url(r'^kontakti/$', views.kontakti, name='kontakti'),
    url(r'', include('katalog.urls')),
]
