from django.urls import path
from .views import PlaceholderView

urlpatterns = [
  # User & Token Endpoints
	# These endpoints are exposed through the /auth routes

  # ...
  path('placeholder', PlaceholderView.as_view()),
]