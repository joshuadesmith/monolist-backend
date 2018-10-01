import boto3

from api.dal.config.config import ENDPOINT_URL, TABLE_NAME


class MonoListDynamoAccess:
    def __init__(self):
        self.dynamo_client = boto3.client('dynamodb', endpoint_url=ENDPOINT_URL)

    def get_item(self, node_source: str, node_sink: str):
        response = self.dynamo_client.get_item(
            TableName=TABLE_NAME,
            Key={
                'node_source': node_source,
                'node_sink': node_sink
            }
        )

        if 'Item' in response:
            return response['Item']

        raise RuntimeError(f"Item with source: {node_source} and sink: {node_sink} does not exist")

    def put_item(self, item: dict):
        response = self.dynamo_client.put_item(
            TABLE_NAME=TABLE_NAME,
            Item=item,
            ReturnValues='UPDATED_NEW',
        )

        if 'Attributes' in response:
            return response['Attributes']

        raise RuntimeError("Error occurred while putting item in database")

    def update_item(self, node_source: str, node_sink: str, attrs: dict):
        response = self.dynamo_client.update_item(
            TableName=TABLE_NAME,
            Key={
                'node_source': node_source,
                'node_sink': node_sink
            },
            AttributeUpdates=attrs,
            ReturnValues='UPDATED_NEW'
        )

        if 'Attributes' in response:
            return response['Attributes']

        raise RuntimeError("Error occurred while updating item in database")
