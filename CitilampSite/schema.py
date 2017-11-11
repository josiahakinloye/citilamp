import graphene

import citilamp.schema as citilampschema
class Query(citilampschema.Query,graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to this project
    pass

schema = graphene.Schema(query=Query)