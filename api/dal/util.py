# Helper methods for getting ID strings for DynamoDB Primary keys
class NodeIDGenerator:
    @staticmethod
    def get_user_node_id(email):
        return f"user-{str(hash(email))}"


def convert_to_camelcase(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))
