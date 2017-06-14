# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Hotel(models.Model):
    owner = models.ForeignKey('auth.User', related_name='hotels', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rating = models.IntegerField()

class Apartment(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='apartments', on_delete=models.CASCADE)
    number = models.IntegerField()
    roomsAmount = models.IntegerField()

class Booking(models.Model):
    client = models.ForeignKey('auth.User', related_name='bookings', on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, related_name='bookings', on_delete=models.CASCADE)
    arrival = models.DateField()
    departure = models.DateField()
    guests = models.IntegerField()
    price = models.IntegerField(default=0)

