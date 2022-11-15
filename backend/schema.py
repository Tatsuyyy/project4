import graphene

import sample.schema


class Query(sample.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(
    query=Query,
)
