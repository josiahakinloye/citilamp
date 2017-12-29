from django.contrib import admin

from citilamp.models import (Beach, City, Continent, Country, Gallery, HistoricalAttraction,MarketTradingcenterSHOP,
                             Museum, Park, Partner, PartnerTag, StateProvince,TouristCenter)

models_to_register = (Beach, City, Continent, Country, Gallery, HistoricalAttraction,MarketTradingcenterSHOP,
                             Museum, Park, Partner, PartnerTag, StateProvince,TouristCenter)

class CitilampBaseAdmin(admin.ModelAdmin):
    search_fields = ('name',)


for model in models_to_register:
    admin.site.register(model, admin_class=CitilampBaseAdmin)