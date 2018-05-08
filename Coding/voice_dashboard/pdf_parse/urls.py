from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^v1', views.upload_file, name='v1'),
    url(r'^pdf_parse',views.parse_pdf, name='parse_pdf')
]