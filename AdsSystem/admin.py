from django.contrib import admin

from AdsSystem.models import Ads

class AdsAdmin(admin.ModelAdmin):
    """
    Admin class used to register the Ads model, you can configure how the Ads
    behaves at the admin end here
    """
    list_display= ('description', 'start_date','stop_date', 'owner_name', 'owner_phone_number','owner_email','approved', 'has_expired',)
    list_filter = ('stop_date',)

admin.site.register(Ads, AdsAdmin)