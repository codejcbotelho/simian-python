import unittest
import botocore.session
from botocore.stub import Stubber
import boto3
from unittest.mock import patch

from app.service.SimianService import SimianService


session = botocore.session.get_session()


class TestSimianRepository(unittest.TestCase):

    response = {'count_mutant_dna': 2, 'count_human_dna': 2, 'ratio': 1.0}

    def setUp(self) -> None:
        pass

    def test_get_stats(self):
        with patch.object(SimianService, "__init__", lambda x, y, z: None)
            s = SimianService(['A', 'B'])
            print('>>>', s.is_simian())

    def test_get_statss(self):
        ddb = session.create_client(
            'dynamodb',
            region_name='us-east-1'
        )
        response = {
            'ResponseMetadata': {
                'RequestId': 'BSHVOTQP7UNJKAMSB4OD32NOPJVV4KQNSO5AEMVJF66Q9ASUAAJG',
                'HTTPStatusCode': 200
            }
        }

        with Stubber(ddb) as stubber:
            stubber.add_response('get_stats', response, {'TableName': 'simian'})
            ddb.describe_table(TableName='simian')

    def test_qualquer(self):
        user_id = 'user123'
        get_item_params = {'TableName': ANY,
                           'Key': {'id': user_id}}
        get_item_response = {}
        ddb_stubber.add_response('get_item', get_item_response, get_item_params)

        result = main.get_user(user_id)
        assert result is None
        ddb_stubber.assert_no_pending_responses()
