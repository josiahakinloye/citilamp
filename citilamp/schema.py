import graphene
from graphene_django.types import DjangoObjectType


from . models import *
class CountryType(DjangoObjectType):
    class Meta:
        model = Country
class ContinentType(DjangoObjectType):
    class Meta:
        model = Continent
class Query(object):
    all_countries = graphene.List(CountryType)
    all_continents = graphene.List(ContinentType)
    continents = graphene.Field(ContinentType,name=graphene.String())
    country = graphene.Field(CountryType,name=graphene.String())
    def resolve_all_continents(self, info, **kwargs):
        return Continent.objects.all()
    def resolve_all_countries(self, info, **kwargs):
        return Country.objects.select_related('continent').all()
    def resolve_country(self, info, **kwargs):
        name = kwargs.get('name')
        try:
            return Country.objects.get(pk=name)
        except Exception as e:
            print(e.message)
    def resolve_continents(self, info, **kwargs):
        name = kwargs.get('name')
        try:
            return Continent.objects.get(pk=name)
        except Exception as e:
            print(e.message)

