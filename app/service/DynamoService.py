import boto3
import settings
import os


class DynamoService(object):

    @staticmethod
    def table(table: str):
        resource = boto3.resource(
            'dynamodb',
            region_name="us-east-1"
        )
        return resource.Table(table)
