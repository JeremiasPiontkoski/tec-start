from rest_framework import serializers
from news.models import New
from location.models import Address, Location
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('id', 'title', 'link')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'street', 'number', 'neighborhood')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'city', 'address', 'cep')

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(request=self.context.get('request'), email=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid email or password")

        data['user'] = user
        return data

from city.models import City
from rest_framework import generics
from news.models import New
from donation.models import Donation
from call.models import Call

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'

class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = '__all__'

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'