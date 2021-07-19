from django.urls import path
from . import views

app_name = 'slatt'
urlpatterns = [
	path('', views.index, name='index'),
]