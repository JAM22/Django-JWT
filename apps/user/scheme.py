from graphene_django import DjangoObjectType
import graphene
from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return User.objects.all()


schema = graphene.Schema(query=Query)