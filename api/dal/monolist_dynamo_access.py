import boto3

from api.dal.config.config import ENDPOINT_URL, TABLE_NAME


class MonoListDynamoAccess:
    def __init__(self):
        self.resource = boto3.resource('dynamodb', endpoint_url=ENDPOINT_URL)
        self.table = self.resource.Table(TABLE_NAME)

    def get_item(self, node_source: dict, node_sink: dict):
        response = self.table.get_item(
            Key={
                'node_source': node_source,
                'node_sink': node_sink
            }
        )

        return response

    def put_item(self, item: dict):
        response = self.table.put_item(
            Item=item,
            ReturnValues='ALL_OLD',
        )

        return response

    def update_item(self, node_source: dict, node_sink: dict, attrs: dict):
        response = self.table.update_item(
            Key={
                'node_source': node_source,
                'node_sink': node_sink
            },
            AttributeUpdates=attrs,
            ReturnValues='ALL_OLD'
        )

        return response
