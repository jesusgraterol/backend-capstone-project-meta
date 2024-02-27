from django.db.models import Model, CharField, SmallIntegerField, DateTimeField, DecimalField

# Create your models here.

class Booking(Model):
  name = CharField(max_length = 255)
  no_of_guests = SmallIntegerField()
  booking_date = DateTimeField()


class Menu(Model):
  title = CharField(max_length = 255)
  price = DecimalField(max_digits = 10, decimal_places = 2)
  inventory = SmallIntegerField()