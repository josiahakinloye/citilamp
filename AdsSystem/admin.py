from django.contrib import admin

# Register your models here.
from AdsSystem.models import Ads
class AdsAdmin(admin.ModelAdmin):
    list_display= ('description', 'start_date','stop_date', 'owner_name', 'owner_phone_number','owner_email','approved', 'has_expired',)
    list_filter = ('stop_date',)
admin.site.register(Ads, AdsAdmin)