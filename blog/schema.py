from django.db.models import Q

import graphene
from graphene_django.types import DjangoObjectType

from .models import Post
from .views import searched_posts


class PostType(DjangoObjectType):
    class Meta:
        model =Post
        exclude_fields = ["image",]


class Query(object):
    all_posts = graphene.List(PostType)
    query_posts = graphene.List(PostType,query_param=graphene.String())

    def resolve_all_posts(self, info, *args, **kwargs):
        return Post.objects.active()

    def resolve_query_posts(self, info, *args, **kwargs):
        parameter_to_query_with = kwargs.get("query_param")
        return searched_posts(parameter_to_query_with)
