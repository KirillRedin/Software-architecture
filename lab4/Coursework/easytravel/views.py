# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import  HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import generics, permissions
from easytravel.models import Hotel, Apartment, Booking
from easytravel.serializers import HotelSerializer, UserSerializer, ApartmentSerializer, BookingSerializer
from easytravel.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

# Create your views here.


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class HotelList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class HotelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class ApartmentList(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    def perform_create(self, serializer):
        serializer.save()

class ApartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly)

class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    hotels = Hotel.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly)
