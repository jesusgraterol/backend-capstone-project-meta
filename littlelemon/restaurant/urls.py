from django.urls import path
from .views import index

urlpatterns = [
  # index
  path('', index, name = 'index'),
  path('home/', index, name = 'home'),

  # ...
  
]