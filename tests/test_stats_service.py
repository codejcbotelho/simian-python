import unittest
import boto3
import botocore.session
from botocore.stub import Stubber, ANY

from moto import mock_dynamodb2
from app.repository.SimianRepository import SimianRepository


class TestStatsService(unittest.TestCase):

    @mock_dynamodb2
    def test_stats(self):
        # mock_stats = {'count_mutant_dna': 0, 'count_human_dna': 0, 'ratio': 0.0}
        # simian_repository.get_stats.return_value = mock_stats

        client = boto3.client(
            'dynamodb',
            region_name='us-east-1'
        )
        stub = Stubber(client)

        response = {
            'ResponseMetadata': {
                'RequestId': 'BSHVOTQP7UNJKAMSB4OD32NOPJVV4KQNSO5AEMVJF66Q9ASUAAJG',
                'HTTPStatusCode': 200
            },
            'Items': [
                {
                    'dna': {
                        "S": 'AAAA:AAAA:AAAA:AAAA'
                    },
                    'type': {
                        "S": '1'
                    }
                }
            ]
        }
        expected_params = {
            'TableName': 'teste'
        }

        client.put_item(Item={
            "dna": {
                "S": "AAA:AAA"
            },
            "type": {
                "S": "1"
            }
        })

        stub.add_response('scan', response, expected_params)
        client.Table('teste')

        with stub:
            print(">>>", client.scan())
