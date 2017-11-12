import graphene
from graphene_django.types import DjangoObjectType

from . models import *



class TravelChoicesEnum(graphene.Enum):
    air = "Air"
    plane= "Plane"
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
        model  = HistoricalAttraction

def makeQueries(Type):
    """
    Make graphql queries for the type passed in
    :param Type: Class
    :return:
    """
    return graphene.List(Type), graphene.Field(Type, name = graphene.String())
class Query(object):
    """
    Class that contains all resolver functions for graphql queries relating to citilamp
    """
    #all_continents = graphene.List(ContinentType)
    #continent = graphene.Field(ContinentType,name=graphene.String())
    all_continents, continent = makeQueries(ContinentType)

    all_countries, country = makeQueries(CountryType)

    all_states_and_provinces, state_and_province = makeQueries(StateProvinceType)

    all_cities, city = makeQueries(CityType)

    all_parks, park = makeQueries(ParkType)

    all_tourist_centers , tourist_center = makeQueries(TouristCenterType)

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
    def resolve_country(self, info, *args,  **kwargs):
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
    """
        def resolve_all_parks(self, info, *args, **kwargs):
            return Park.objects.select_related('city_or_country').all()
    """
    #lastthoughts make city_or_country field related probably crate a new field or class or can the front end construct a query that checks if city or country was passed in then determine what to do or just query for mesum set directly from county or city
    """
    def resolve_all_museums(self, info, *args, **kwargs):
        return Museum.objects.select_related('city_or_country').all()
    """

