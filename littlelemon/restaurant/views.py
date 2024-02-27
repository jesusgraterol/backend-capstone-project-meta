from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, \
DestroyAPIView 
from rest_framework.viewsets import ModelViewSet

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer

# Create your views here.


#############
# GUI VIEWS #
#############

def index(request):
  return render(request, 'index.html', {})




#################
# BOOKING VIEWS #
#################

class BookingViewSet(ModelViewSet):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer
  # permission_classes = [ IsAuthenticated ] 



##############
# MENU VIEWS #
##############

class MenuItemsView(ListAPIView, CreateAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer