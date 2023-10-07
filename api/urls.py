from django.urls import path
from . import views

urlpatterns = [
    path('addresses/', views.get_all_addresses, name='get_all_addresses'),
    path('addresses/<int:pk>/', views.get_address_by_id, name='get_address_by_id'),
    path('addresses/register/', views.register_address, name='register_address'),
    path('locations/', views.get_all_locations, name='get_all_locations'),
    path('locations/<int:pk>/', views.get_location_by_id, name='get_location_by_id'),
    path('locations/register/', views.register_location, name='register_location'),
    path('login/', views.LoginAPIView.as_view(), name='user-login'),

    path('news/', views.NewListCreateView.as_view(), name='get-news'),
    path('cities/', views.CityListCreateView.as_view(), name='get-cities'),
    path('calls/', views.CallListCreateView.as_view(), name='get-calls'),
    path('donations/', views.DonationCreateView.as_view(), name='get-donations')
]