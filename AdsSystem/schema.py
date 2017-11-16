import graphene
from graphene_django import DjangoObjectType

from .models import Ads

class AdsType(DjangoObjectType):

    class Meta:
        model = Ads


class Query(object):
    """
    This contains graphql queries and their respective resolver functions
    """
    approved_ads = graphene.List(AdsType)

    def resolve_approved_ads(self, info, *args, **kwargs):
        return Ads.objects.filter(approved=True,)