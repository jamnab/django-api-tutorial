from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'ˆproducts/$', views.product_list),
]