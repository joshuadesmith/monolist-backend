from api.dal.monolist_dynamo_access import MonoListDynamoAccess
from api.dal.util import NodeIDGenerator

db_access = MonoListDynamoAccess()


# API methods to be called by Graphene Queries/Mutations
def get_user(email: str) -> dict:
    user_id = NodeIDGenerator.get_user_node_id(email)

    try:
        user_dict = db_access.get_item(user_id, user_id)
        return user_dict
    except RuntimeError as e:
        return {}


def put_user(user_dict: dict) -> dict:
    assert 'email' in user_dict

    user_id = NodeIDGenerator.get_user_node_id(user_dict['email'])
    attr_dict = user_dict
    attr_dict['node_source'] = user_id
    attr_dict['node_sink'] = user_id

    try:
        resp = db_access.put_item(attr_dict)
        return resp
    except RuntimeError as e:
        return {}


def update_user(email: str, updated_attr: dict) -> dict:
    user_id = NodeIDGenerator.get_user_node_id(email)

    try:
        resp = db_access.update_item(user_id, user_id, updated_attr)
        return resp
    except RuntimeError as e:
        return {}
