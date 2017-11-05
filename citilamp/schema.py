import graphene
from graphene_django.types import DjangoObjectType


from . models import *
class CountryType(DjangoObjectType):
    class Meta:
        model = Country
class Query(object):
    all_countries = graphene.List(CountryType)
    def resolve_all_categories(self, info, **kwargs):
        return Country.objects.all()