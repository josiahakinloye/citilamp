"""Contains everything graph ql with respect to AdsSystem"""
import graphene
from graphene_django import DjangoObjectType

from .models import Ads


class AdsType(DjangoObjectType):
    """
    Type that maps to the Ads  model
    """
    class Meta:
        """
        Meta class for AdsType class this is where you pass in
        the name of model you want graph ql  to use
        """
        model = Ads


class Query(object):
    """
    Graph ql query for the ads model
    """
    # a list of valid ads
    valid_ads = graphene.List(AdsType)

    def resolve_valid_ads(self, info, *args, **kwargs):
        approved_ads = Ads.objects.filter(approved=True,)
        approved_and_not_expired =  [ad for ad in approved_ads if  not (ad.has_expired())]
        return approved_and_not_expired