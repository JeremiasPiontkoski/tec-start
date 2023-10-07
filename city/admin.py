from django.contrib import admin
from news.models import New
from donation.models import Donation
from call.models import Call
from .models import City

class NewsInline(admin.TabularInline):
    model = New
    extra = 1

class DonationInline(admin.TabularInline):
    model = Donation
    extra = 1

class CallInline(admin.TabularInline):
    model = Call
    extra = 1

class CityAdmin(admin.ModelAdmin):
    inlines = [NewsInline, DonationInline, CallInline]

admin.site.register(City, CityAdmin)
