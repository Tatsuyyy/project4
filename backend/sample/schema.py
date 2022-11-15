import graphene
from graphene_django import DjangoObjectType

from sample.models import Items


class Item(DjangoObjectType):
    class Meta:
        model = Items


class Query(graphene.ObjectType):
    items = graphene.List(Item)

    def resolve_items(self, info, **kwargs):
        return Items.objects.all()
