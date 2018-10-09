from api.dal.monolist_dynamo_access import MonoListDynamoAccess
from api.dal.util import NodeIDGenerator

db_access = MonoListDynamoAccess()


# API methods to be called by Graphene Queries/Mutations
def get_user(email: str) -> dict:
    user_id = NodeIDGenerator.get_user_node_id(email)

    resp = db_access.get_item(user_id, user_id)
    if 'Item' in resp:
        return resp['Item']

    raise RuntimeError(f'No user found with email "{email}"')


def put_user(user_dict: dict) -> dict:
    assert 'email' in user_dict

    user_id = NodeIDGenerator.get_user_node_id(user_dict['email'])
    attr_dict = user_dict
    attr_dict['node_source'] = user_id
    attr_dict['node_sink'] = user_id

    resp = db_access.put_item(attr_dict)
    if 'Item' in resp:
        return resp['Item']

    raise RuntimeError(f'Error occurred while creating user with email "{user_dict["email"]}"')


def update_user(email: str, updated_attr: dict) -> dict:
    """ Right now this replaces the entire user object for simplicity """
    user_id = NodeIDGenerator.get_user_node_id(email)

    user_item = dict()
    user_item['node_source'] = user_id
    user_item['node_sink'] = user_id
    for key, val in updated_attr.items():
        user_item[key] = val

    resp = db_access.put_item(user_item)
    if 'Item' in resp:
        return resp['Item']

    raise RuntimeError(f'Could not update user object with email "{email}"')
