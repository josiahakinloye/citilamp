import graphene
from graphene_django.types import DjangoObjectType

from citilamp.models import (Continent, Country, StateProvince, City, Park, Museum, TouristCenter, Gallery, MarketTradingcenterSHOP, HistoricalAttraction, Beach)

class TravelChoicesEnum(graphene.Enum):
    air = "Air"
    plane = "Plane"
    bus = "Bus"
    train = "Train"

class ContinentType(DjangoObjectType):
    class Meta:
        model = Continent


class CountryType(DjangoObjectType):
    entry_requirement = TravelChoicesEnum()
    class Meta:
        model = Country


class StateProvinceType(DjangoObjectType):
    class Meta:
        model = StateProvince


class CityType(DjangoObjectType):
    entry_requirement = TravelChoicesEnum()
    class Meta:
        model = City

class ParkType(DjangoObjectType):
    class Meta:
        model = Park

class TouristCenterType(DjangoObjectType):
    class Meta:
        model = TouristCenter


class BeachType(DjangoObjectType):
    class Meta:
        model = Beach


class MuseumType(DjangoObjectType):
    class Meta:
        model = Museum

class GalleryType(DjangoObjectType):
    class Meta:
        model = Gallery

class MarketTradingcenterSHOPType(DjangoObjectType):
    class Meta:
        model = MarketTradingcenterSHOP


class HistoricalAttractionType(DjangoObjectType):
    class Meta:
        model = HistoricalAttraction

def makeQueries(typeToMakeQueryFieldsFor):
    """
    Make graphql queries for the type passed in
    :param typeToMakeQueryFieldsFor: Class
    :return:
    """
    return graphene.List(typeToMakeQueryFieldsFor), graphene.Field(typeToMakeQueryFieldsFor, name=graphene.String())


class Query(object):
    """
    Class that contains all resolver functions for graphql queries relating to citilamp
    """

    all_continents, continent = makeQueries(ContinentType)

    all_countries, country = makeQueries(CountryType)

    all_states_and_provinces, state_and_province = makeQueries(StateProvinceType)

    all_cities, city = makeQueries(CityType)

    all_parks, park = makeQueries(ParkType)

    all_tourist_centers, tourist_center = makeQueries(TouristCenterType)

    all_beaches, beach = makeQueries(BeachType)

    all_museums, museum = makeQueries(MuseumType)

    all_galleries, gallery = makeQueries(GalleryType)

    all_markets_tradingcenters_shops, market_tradingcenter_shop = makeQueries(MarketTradingcenterSHOPType)

    all_historical_attractions, historical_attraction = makeQueries(HistoricalAttractionType)


    def resolve_all_continents(self, info, *args, **kwargs):
        return Continent.objects.all()

    def resolve_continent(self, info, *args, **kwargs):
        name = kwargs.get('name')
        return Continent.objects.get(pk=name)


    def resolve_all_countries(self, info, *args, **kwargs):
        return Country.objects.select_related('continent').all()

    def resolve_country(self, info, *args, **kwargs):
        name = kwargs.get('name')
        return Country.objects.get(pk=name)


    def resolve_all_states_and_provinces(self, info, *args, **kwargs):
        return StateProvince.objects.select_related('country').all()

    def resolve_state_and_province(self, info, *args, **kwargs):
        name = kwargs.get('name')
        return StateProvince.objects.get(pk=name)


    def resolve_all_cities(self, info, *args, **kwargs):
        return City.objects.select_related('stateprovince').all()

    def resolve_city(self, info, *args, **kwargs):
        name = kwargs.get('name')
        return City.objects.get(pk=name)


    def resolve_all_parks(self, info, *args, **kwargs):
        #Since park is related to both city and country
        if Park.objects.select_related("city").all():
            return Park.objects.select_related("city").all()
        if Park.objects.select_related("country").all():
            return Park.objects.select_related("country").all()

    def resolve_park(self, info, *args, **kwargs):
        name = kwargs.get('name')
        return Park.objects.get(pk=name)

    def resolve_all_tourist_centers(self, info, *args, **kwargs):
        if TouristCenter.objects.select_related("city").all():
            return TouristCenter.objects.select_related("city").all()
        if TouristCenter.objects.select_related("country").all():
            return TouristCenter.objects.select_related("country").all()

    def resolve_tourist_center(self, info, *args, **kwargs):
        name = kwargs.get('name')
        return TouristCenter.objects.get(pk=name)



    def resolve_all_beaches(self, info, *args, **kwargs):
        if Beach.objects.select_related("city").all():
            return Beach.objects.select_related("city").all()
        if Beach.objects.select_related("country").all():
            return Beach.objects.select_related("country").all()

    def resolve_beach(self, info, *args, **kwargs):
        name = kwargs.get('name')
        return Beach.objects.get(pk=name)

    def resolve_all_museums(self, info, *args, **kwargs):
        if Museum.objects.select_related("city").all():
            return Museum.objects.select_related("city").all()
        if Museum.objects.select_related("country").all():
            return Museum.objects.select_related("country").all()


    def resolve_museum(self, info, *args, **kwargs):
        name = kwargs.get('name')
        return Museum.objects.get(pk=name)

    def resolve_all_galleries(self, info, *args, **kwargs):
        if Gallery.objects.select_related("city").all():
            return Gallery.objects.select_related("city").all()
        if Gallery.objects.select_related("country").all():
            return Gallery.objects.select_related("country").all()

    def resolve_gallery(self, info, *args, **kwargs):
        name = kwargs.get('name')
        return Gallery.objects.get(pk=name)

    def resolve_all_markets_tradingcenters_shops(self, info, *args, **kwargs):
        if MarketTradingcenterSHOP.objects.select_related("city").all():
            return MarketTradingcenterSHOP.objects.select_related("city").all()
        if MarketTradingcenterSHOP.objects.select_related("country").all():
            return MarketTradingcenterSHOP.objects.select_related("country").all()

    def resolve_market_tradingcenter_shop(self, info, *args, **kwargs):
        name = kwargs.get('name')
        return MarketTradingcenterSHOP.objects.get(pk=name)

    def resolve_all_historical_attractions(self, info, *args, **kwargs):
        if HistoricalAttraction.objects.select_related("city").all():
            return HistoricalAttraction.objects.select_related("city").all()
        if HistoricalAttraction.objects.select_related("country").all():
            return HistoricalAttraction.objects.select_related("country").all()

    def resolve_historical_attraction(self, info, *args, **kwargs):
        name = kwargs.get('name')
        return HistoricalAttraction.objects.get(pk=name)
