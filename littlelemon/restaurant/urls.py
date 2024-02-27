from django.urls import path
from .views import index, MenuItemsView, SingleMenuItemView

urlpatterns = [
  # index
  path('', index, name = 'index'),
  path('home/', index, name = 'home'),

  # menu
  path('menu/', MenuItemsView.as_view()),
  path('menu/<int:pk>', SingleMenuItemView.as_view()),
  
]