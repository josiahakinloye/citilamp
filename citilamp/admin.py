from django.contrib import admin

from citilamp.models import (Continent, Country, StateProvince, City, Park, Museum, TouristCenter ,
                              Gallery, MarketTradingcenterSHOP, HistoricalAttraction, Beach, Tag, Partner)

models_to_register = (Continent, Country, StateProvince, City, Park, Museum, TouristCenter ,Gallery,
                      MarketTradingcenterSHOP, HistoricalAttraction, Beach, Tag, Partner)


class CitilampBaseAdmin(admin.ModelAdmin):
    search_fields = ('name',)


for model in models_to_register:
    admin.site.register(model, admin_class=CitilampBaseAdmin)