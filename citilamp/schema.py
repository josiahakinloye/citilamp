from django.db.models import Q

import graphene
from graphene_django.types import DjangoObjectType

from citilamp.models import (Beach, City, Continent, Country, Gallery, HistoricalAttraction, MarketTradingcenterSHOP,
                             Museum, Park, Partner, PartnerTag, StateProvince, TouristCenter)


class TravelChoicesEnum(graphene.Enum):
    """
    For travel choices ... Since graph ql does not handle enums well
    """
    air = "Air"
    plane = "Plane"
    bus = "Bus"
    train = "Train"


class ContinentType(DjangoObjectType):
    """
    Type that maps to the Continent model
    used to graph ql to understand the model's fields
    """

    class Meta:
        model = Continent


class CountryType(DjangoObjectType):
    """
    Type that maps to the Country model
    used to graph ql to understand the model's fields
    """
    entry_requirement = TravelChoicesEnum()

    class Meta:
        model = Country


class StateProvinceType(DjangoObjectType):
    """
    Type that maps to the StateProvince  model
    used to graph ql to understand the model's fields
    """
    class Meta:
        model = StateProvince


class CityType(DjangoObjectType):
    """
    Type that maps to the City  model
    used to graph ql to understand the model's fields
    """
    entry_requirement = TravelChoicesEnum()

    class Meta:
        model = City


class ParkType(DjangoObjectType):
    """
    Type that maps to the Park  model
    used to graph ql to understand the model's fields
    """
    class Meta:
        model = Park


class TouristCenterType(DjangoObjectType):
    """
    Type that maps to the TouristCenter  model
    used to graph ql to understand the model's fields
    """
    class Meta:
        model = TouristCenter


class BeachType(DjangoObjectType):
    """
    Type that maps to the Beach  model
    used to graph ql to understand the model's fields
    """
    class Meta:
        model = Beach


class MuseumType(DjangoObjectType):
    """
    Type that maps to the museum model
    used to graph ql to understand the model's fields
    """
    class Meta:
        model = Museum


class GalleryType(DjangoObjectType):
    """
    Type that maps to the Gallery  model
    used to graph ql to understand the model's fields
    """
    class Meta:
        model = Gallery


class MarketTradingcenterSHOPType(DjangoObjectType):
    """
    Type that maps to the MarketTradingcenterSHOP model
    used to graph ql to understand the model's fields
    """
    class Meta:
        model = MarketTradingcenterSHOP


class HistoricalAttractionType(DjangoObjectType):
    """
    Type that maps to the HistoricalAttraction model
    used to graph ql to understand the model's fields
    """
    class Meta:
        model = HistoricalAttraction


class PartnerTagType(DjangoObjectType):
    """
    Type that maps to the PartnerTag model
    """

    class Meta:
        model = PartnerTag


class PartnerType(DjangoObjectType):
    """
    Type that maps to the partner model
    """

    class Meta:
        model = Partner


def make_queries(typeToMakeQueryFieldsFor):
    """
    Make graphql queries for the type passed in
    :param typeToMakeQueryFieldsFor: Class
    :return: tuple graphene list and a graphene field
    """
    return graphene.List(typeToMakeQueryFieldsFor), graphene.Field(typeToMakeQueryFieldsFor, name=graphene.String())


def city_country_set(model):

    @property
    def get_objects(model):
        return model.objects

    try:
        return get_objects.select_related("city").all()
    except:
        return get_objects.select_related("country").all()

class Query(object):
    """
    Class that contains all resolver functions for graph ql queries relating to core  citilamp models
    """

    all_continents, continent = make_queries(ContinentType)

    all_countries, country = make_queries(CountryType)

    all_states_and_provinces, state_and_province = make_queries(StateProvinceType)

    all_cities, city = make_queries(CityType)

    all_parks, park = make_queries(ParkType)

    all_tourist_centers, tourist_center = make_queries(TouristCenterType)

    all_beaches, beach = make_queries(BeachType)

    all_museums, museum = make_queries(MuseumType)

    all_galleries, gallery = make_queries(GalleryType)

    all_markets_tradingcenters_shops, market_tradingcenter_shop = make_queries(MarketTradingcenterSHOPType)

    all_historical_attractions, historical_attraction = make_queries(HistoricalAttractionType)

    all_partner_tags, partner_tag = make_queries(PartnerTagType)

    # location : city,country. String used to query address and areas of operation fields eg.Ikeja, Lagos or Usa
    partners = graphene.List(PartnerType, area=graphene.String(), tag=graphene.String())

    # Graphql resolver functions
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
        city_country_set(Park)

    def resolve_park(self, info, *args, **kwargs):
        name = kwargs.get('name')
        return Park.objects.get(pk=name)

    def resolve_all_tourist_centers(self, info, *args, **kwargs):
        city_country_set(TouristCenter)

    def resolve_tourist_center(self, info, *args, **kwargs):
        name = kwargs.get('name')
        return TouristCenter.objects.get(pk=name)

    def resolve_all_beaches(self, info, *args, **kwargs):
        city_country_set(Beach)

    def resolve_beach(self, info, *args, **kwargs):
        name = kwargs.get('name')
        return Beach.objects.get(pk=name)


    def resolve_all_museums(self, info, *args, **kwargs):
        city_country_set(Museum)

    def resolve_museum(self, info, *args, **kwargs):
        name = kwargs.get('name')
        return Museum.objects.get(pk=name)

    def resolve_all_galleries(self, info, *args, **kwargs):
        city_country_set(Gallery)

    def resolve_gallery(self, info, *args, **kwargs):
        name = kwargs.get('name')
        return Gallery.objects.get(pk=name)

    def resolve_all_markets_tradingcenters_shops(self, info, *args, **kwargs):
        city_country_set(MarketTradingcenterSHOP)

    def resolve_market_tradingcenter_shop(self, info, *args, **kwargs):
        name = kwargs.get('name')
        return MarketTradingcenterSHOP.objects.get(pk=name)

    def resolve_all_historical_attractions(self, info, *args, **kwargs):
        city_country_set(HistoricalAttraction)

    def resolve_historical_attraction(self, info, *args, **kwargs):
        name = kwargs.get('name')
        return HistoricalAttraction.objects.get(pk=name)

    def resolve_all_partner_tags(self, info, *args, **kwargs):
        return PartnerTag.objects.all()

    def resolve_partner_tag(self, info, *args, **kwargs):
        name = kwargs.get('name')
        return PartnerTag.objects.get(pk=name)

    def resolve_partners(self, info, *args, **kwargs):
        area = kwargs.get('area').replace(' ', '')
        tag = kwargs.get('tag')
        partners_list = Partner.objects.filter(tag=tag).filter(Q(address__icontains=area) |
                                                               Q(areas_of_operation__icontains=area))
        return partners_list
