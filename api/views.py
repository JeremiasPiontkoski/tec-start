# from django.shortcuts import render
from rest_framework import status, serializers
from rest_framework.response import Response
from .serializers import AddressSerializer, LocationSerializer, LoginSerializer
from location.models import Address, Location
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
# from .serializers import CustomUserSerializer
from news import models
# from location.models import Location
# from user.models import CustomUser
# from knox.models import AuthToken
# from rest_framework.permissions import AllowAny
# from knox.views import LoginView as KnoxLoginView
# from rest_framework import permissions
# from django.contrib.auth import authenticate, login
# from rest_framework.views import APIView
# from rest_framework.authtoken.models import Token

@api_view(['GET'])
def get_news(request):
    news = models.New.objects.all()
    serializer = serializers.NewSerializer(news, many=True)
    return Response({'news': serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_addresses(request):
    addresses = Address.objects.all()
    serializer = AddressSerializer(addresses, many=True)
    return Response({'addresses': serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_address_by_id(request, pk):
    try:
        address = Address.objects.get(pk=pk)
    except Address.DoesNotExist:
        return Response(status=404)

    serializer = AddressSerializer(address)
    return Response({'address': serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def register_address(request):
    serializer = AddressSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'address': serializer.data}, status=status.HTTP_201_CREATED)
    return Response({'errors': serializer.errors}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def get_all_locations(request):
    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)
    return Response({'locations': serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_location_by_id(request, pk):
    try:
        locations = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = LocationSerializer(locations)
    return Response({'location': serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def register_location(request):
    serializer = LocationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'location': serializer.data}, status=status.HTTP_201_CREATED)
    return Response({'errors': serializer.errors}, status=status.HTTP_401_UNAUTHORIZED)

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .serializers import CitySerializer, CallSerializer, DonationSerializer, NewSerializer
from rest_framework import generics
from city.models import City
from news.models import New
from call.models import Call
from donation.models import Donation

class CityListCreateView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class NewListCreateView(generics.ListCreateAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer

class CallListCreateView(generics.ListCreateAPIView):
    queryset = Call.objects.all()
    serializer_class = CallSerializer

class DonationCreateView(generics.ListCreateAPIView):
    queryset = Donation.objects.all().order_by('-date_send')
    serializer_class = DonationSerializer