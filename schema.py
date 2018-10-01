# Definitions of GraphQL object types, queries, mutations, and schema
import graphene


class UserObject(graphene.ObjectType):
    user_email = graphene.String()
    spotify_auth_code = graphene.String()


class Query(graphene.ObjectType):
    user_by_email = graphene.Field(graphene.String, email=graphene.String())

    def resolve_user_by_email(self, info, **kwargs):
        return f"Test {kwargs.get('email')}"


schema = graphene.Schema(query=Query)
