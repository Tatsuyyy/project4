import graphene

import earap.schema


class Query(earap.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(
    query=Query,
)
