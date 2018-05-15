from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^form/$', views.upload_form),
    url(r'^upload/$', views.upload_multi_file),
]