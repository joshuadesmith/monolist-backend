# Helper methods for getting ID strings for DynamoDB Primary keys
import base64
import hashlib


class NodeIDGenerator:
    @staticmethod
    def get_user_node_id(email):
        return f"user-{NodeIDGenerator.generate_hashed_id(email)}"

    @staticmethod
    def generate_hashed_id(s):
        encoded = s.encode('utf-8')
        b64 = base64.b64encode(hashlib.md5(encoded).digest())
        return str(b64)


def convert_to_camelcase(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))
