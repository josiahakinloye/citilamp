from django.db.models import Q

import graphene
from graphene_django.types import DjangoObjectType

from .models import Post
from .views import searched_posts
from django.contrib.auth.models import User


class PostType(DjangoObjectType):
    class Meta:
        model =Post
        exclude_fields = ["image",]

class AuthorType(DjangoObjectType):
    class Meta:
        model = User


class Query(object):
    post = graphene.Field(PostType, slug=graphene.String())
    all_posts = graphene.List(PostType)
    query_posts = graphene.List(PostType,query_param=graphene.String())

    all_authors = graphene.List(AuthorType)
    author = graphene.Field(AuthorType, user_name=graphene.String())


    def resolve_post(self, info, *args, **kwargs):
        slug = kwargs.get('slug')
        return Post.objects.active().get(slug=slug)

    def resolve_all_posts(self, info, *args, **kwargs):
        return Post.objects.active().select_related('author')

    def resolve_query_posts(self, info, *args, **kwargs):
        parameter_to_query_with = kwargs.get("query_param")
        return searched_posts(parameter_to_query_with)

    def resolve_all_authors(self, info, *args, **kwargs):
        return User.objects.all()

    def resolve_author(self, info, *args, **kwargs):
        user_name = kwargs.get('user_name')
        return User.objects.get(username=user_name)
