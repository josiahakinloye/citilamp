import graphene

import AdsSystem.schema as AdsSystemSchema
import citilamp.schema as citilampschema
<<<<<<< HEAD
from .weather import get_weather_forecast_comparison

class Query(citilampschema.Query, AdsSystemSchema.Query, graphene.ObjectType):
    """
    This class will inherit from multiple Queries
    as we begin to add more apps to this project
    """

    weather_comparison = graphene.JSONString(user_city=graphene.String(), explored_city=graphene.String(), days=graphene.Int())
    def resolve_weather_comparison(self, info, *args, **kwargs):
        """
        Graphql resolver function for weather comparison
        :param info:
        :param args:
        :param kwargs:
        :return:
        """
        user_city, explored_city = kwargs.get('user_city'), kwargs.get('explored_city')
        if kwargs.get('days'):
            days = kwargs.get('days')
            weatherComparison = get_weather_forecast_comparison(user_city=user_city, explored_city=explored_city, days=days)
        else:
            weatherComparison = get_weather_forecast_comparison(user_city=user_city, explored_city=explored_city)
        return list(weatherComparison)
=======
from .exchange import convertCurrency


class Query(citilampschema.Query, AdsSystemSchema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to this project
    convert_currency = graphene.Int(currency_from=graphene.String(), currency_to=graphene.String(), quantity=graphene.Int())

    def resolve_convert_currency(self, info, *args, **kwargs):
        currency_from =kwargs.get('currency_from')
        currency_to = kwargs.get('currency_to')
        quantity = kwargs.get('quantity')
        return convertCurrency(currency_from, currency_to, quantity)
>>>>>>> feature_currency_exchange


schema = graphene.Schema(query=Query)
