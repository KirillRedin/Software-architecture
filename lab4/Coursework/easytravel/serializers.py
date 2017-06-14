from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from easytravel.models import Hotel, Apartment, Booking
from django.contrib.auth.models import User

class ApartmentSerializer(serializers.ModelSerializer):
    hotel = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all())

    class Meta:
        model = Apartment
        fields = ('id', 'hotel', 'number', 'roomsAmount')
        validators = [
            UniqueTogetherValidator(
                queryset=Apartment.objects.all(),
                fields=('hotel', 'number')
            )
        ]

    def create(self, validated_data):
        apartment = Apartment.objects.create(hotel=validated_data['hotel'], number=validated_data['number'],
                                             roomsAmount=validated_data['roomsAmount'])
        return apartment

class HotelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    apartments = ApartmentSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ('id', 'name', 'rating', 'owner', 'apartments')

class BookingSerializer(serializers.ModelSerializer):
    apartment = serializers.PrimaryKeyRelatedField(queryset=Apartment.objects.all())

    class Meta:
        model = Booking
        fields = ('id', 'apartment', 'client', 'arrival', 'departure', 'guests', 'price')

    def create(self, validated_data):
        booking = Booking.objects.create(apartment=validated_data['apartment'], arrival=validated_data['arrival'],
                                         departure=validated_data['departure'], guests=validated_data['guests'],
                                         client = validated_data['client'])
        return booking

class UserSerializer(serializers.ModelSerializer):
    # bookings = BookingSerializer(many=True, read_only=True)
    # hotels = HotelSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username')