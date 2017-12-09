"""Contains everything graphql with respect to AdsSystem"""
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
        the name of model you want graphql  to use
        """
        model = Ads


class Query(object):
    """
    Graphql query for the ads model
    """
    # a list of approved ads
    approved_ads = graphene.List(AdsType)

    def resolve_approved_ads(self, info, *args, **kwargs):
        return Ads.objects.filter(approved=True,)
