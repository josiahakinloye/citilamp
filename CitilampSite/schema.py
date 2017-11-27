import graphene

import AdsSystem.schema as AdsSystemSchema
import citilamp.schema as citilampschema
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


schema = graphene.Schema(query=Query)
