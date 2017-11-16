"""Contains everything graphql with respect to AdsSystem"""
import graphene
from graphene_django import DjangoObjectType

from .models import Ads

class AdsType(DjangoObjectType):
    """
    Graphene model type that maps to the model property given in its meta class
    """
    class Meta:
        """
        Meta class for AdsType class this is where you pass in
        the name of model you want graphql  to use
        """
        model = Ads


class Query(object):
    """
    This contains graphql queries and their respective resolver functions
    """
    approved_ads = graphene.List(AdsType)

    def resolve_approved_ads(self, info, *args, **kwargs):
        return Ads.objects.filter(approved=True,)
