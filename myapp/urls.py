from django.urls import path
from . import views
urlpatterns = [
    path('hi/', views.add, name= 'add'),
]