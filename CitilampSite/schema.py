import graphene

import citilamp.schema as ci
class Query(ci.Query,graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to this project
    pass

schema = graphene.Schema(query=Query)