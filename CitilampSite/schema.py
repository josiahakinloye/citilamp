import graphene

import citilamp.schema as citilampschema
import AdsSystem.schema as AdsSystemSchema


class Query(citilampschema.Query, AdsSystemSchema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to this project
    pass


schema = graphene.Schema(query=Query)
