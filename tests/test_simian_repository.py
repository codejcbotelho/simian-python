import unittest
import botocore.session
import boto3
from unittest.mock import MagicMock
from botocore.stub import Stubber
from app.repository.SimianRepository import SimianRepository


class TestSimianRepository(unittest.TestCase):

    def setUp(self) -> None:
        self.expected_params = {
            'TableName': 'table'
        }
        self.resource = botocore.session.get_session().create_client(
            'dynamodb',
            region_name='us-east-1'
        )

    def test_get_stats_equals(self):

        mock_response = TestSimianRepository.generate_mock(1, 1)
        stats_expected = {'count_mutant_dna': 1, 'count_human_dna': 1, 'ratio': 1.0}

        with Stubber(self.resource) as stub:
            stub.add_response('scan', mock_response, self.expected_params)
            response = self.resource.scan(
                TableName='table'
            )

            simian_repository = SimianRepository()
            simian_repository.table.scan = MagicMock(return_value=response)

            self.assertEqual(SimianRepository.get_stats(), stats_expected)

    def test_get_stats_with_more_mutants(self):

        mock_response = TestSimianRepository.generate_mock(10, 5)
        stats_expected = {'count_mutant_dna': 10, 'count_human_dna': 5, 'ratio': 2.0}

        with Stubber(self.resource) as stub:
            stub.add_response('scan', mock_response, self.expected_params)
            response = self.resource.scan(
                TableName='table'
            )

            simian_repository = SimianRepository()
            simian_repository.table.scan = MagicMock(return_value=response)

            self.assertEqual(SimianRepository.get_stats(), stats_expected)

    def test_get_stats_with_more_humans(self):

        mock_response = TestSimianRepository.generate_mock(1, 20)
        stats_expected = {'count_mutant_dna': 1, 'count_human_dna': 20, 'ratio': 0.05}

        with Stubber(self.resource) as stub:
            stub.add_response('scan', mock_response, self.expected_params)
            response = self.resource.scan(
                TableName='table'
            )

            simian_repository = SimianRepository()
            simian_repository.table.scan = MagicMock(return_value=response)

            self.assertEqual(SimianRepository.get_stats(), stats_expected)

    @classmethod
    def generate_mock(cls, simian: int, human: int):
        item = {'Items': []}

        i = 0
        while i < simian:
            item['Items'].append({
                'dna': {
                    'S': 'A:A:A:A'
                },
                'type': {
                    'S': '1'
                }
            })
            i = i + 1

        z = 0
        while z < human:
            item['Items'].append({
                'dna': {
                    'S': 'A:A:A:A'
                },
                'type': {
                    'S': '0'
                }
            })
            z = z + 1

        return item

