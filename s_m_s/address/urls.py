from django.urls import path
from .views import *

urlpatterns=[
		path('district',views.add_district, name='district'),
		path('upazilla', views.add_upazilla, name='upazilla'),
		path('union', views.add_union, name='union'),
		]