from django.urls import path
from hotwireca.views import *
app_name = 'hotwireca'
urlpatterns = [
    path('home', index, name='index'),
    path('testlang', testlang, name='testlang'),
]

