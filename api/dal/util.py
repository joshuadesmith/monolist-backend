# Helper methods for getting ID strings for DynamoDB Primary keys
class NodeIDGenerator:
    @staticmethod
    def get_user_node_id(email):
        return f"user-{str(hash(email))}"


def convert_dict_for_dynamo(d: dict) -> dict:
    ret = dict()
    for key, val in d.items():
        if isinstance(val, str):
            ret[key] = {"S": val}
        elif isinstance(val, int):
            ret[key] = {"N": val}
    return ret


def convert_to_camelcase(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))
