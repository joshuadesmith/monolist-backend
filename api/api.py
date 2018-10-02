from api.dal.monolist_dynamo_access import MonoListDynamoAccess
from api.dal.util import NodeIDGenerator, convert_dict_for_dynamo

db_access = MonoListDynamoAccess()


# API methods to be called by Graphene Queries/Mutations
def get_user(email: str) -> dict:
    user_id = {"S": NodeIDGenerator.get_user_node_id(email)}
    print(user_id)

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

    resp = db_access.put_item(convert_dict_for_dynamo(attr_dict))
    return resp


def update_user(email: str, updated_attr: dict) -> dict:
    user_id = {"S": NodeIDGenerator.get_user_node_id(email)}
    attrs = convert_dict_for_dynamo(updated_attr)

    resp = db_access.update_item(user_id, user_id, attrs)
    return resp
