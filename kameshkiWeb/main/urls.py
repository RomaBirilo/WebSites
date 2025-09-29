from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('collections/',views.collections, name='collections'),
    path('contacts/',views.contacts, name='contacts'),
]