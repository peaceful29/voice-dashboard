from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^file/$', views.upload_form),
    url(r'^upload/$', views.upload_multi_file),
    # url(r'^uploaded/$', views.parse_to_db),
    url(r'^report/$', views.show_result)
]