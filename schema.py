# Definitions of GraphQL object types, queries, mutations, and schema
import graphene

from api import api


class UserObject(graphene.ObjectType):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for dictionary in args:
            for key, val in dictionary.items():
                setattr(self, key, val)

    user_email = graphene.String()
    spotify_auth_code = graphene.String()


class Query(graphene.ObjectType):
    user_by_email = graphene.Field(UserObject, email=graphene.String())

    def resolve_user_by_email(self, info, **kwargs):
        user_dict = api.get_user(kwargs.get('email'))
        return UserObject(user_dict)


schema = graphene.Schema(query=Query)
