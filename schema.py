# Definitions of GraphQL object types, queries, mutations, and schema
import graphene

from api import api


class UserObject(graphene.ObjectType):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for dictionary in args:
            for key, val in dictionary.items():
                setattr(self, key, val)

    email = graphene.String()
    spotify_auth_code = graphene.String()


class CreateUser(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)

    success = graphene.Boolean()
    new_user = graphene.Field(UserObject)

    def mutate(self, info, **kwargs):
        user_dict = {
            'email': kwargs.get('email')
        }
        resp = api.put_user(user_dict)
        return CreateUser(success=True, new_user=UserObject(email=resp['email']))


class UpdateUser(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        spotify_auth_code = graphene.String(required=False)

    success = graphene.Boolean()
    updated_user = graphene.Field(UserObject)

    def mutate(self, info, **kwargs):
        user_dict = dict()
        for key, val in kwargs.items():
            user_dict[key] = val

        resp = api.update_user(user_dict['email'], user_dict)
        return CreateUser(success=True, updated_user=user_dict)


class UserQuery(graphene.ObjectType):
    user_by_email = graphene.Field(UserObject, email=graphene.String())

    def resolve_user_by_email(self, info, **kwargs):
        user_dict = api.get_user(kwargs.get('email'))
        return UserObject(user_dict)


class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()


schema = graphene.Schema(query=UserQuery, mutation=Mutations)
