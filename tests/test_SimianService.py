import unittest
from unittest.mock import MagicMock
import boto3 

#from moto import mock_dynamodb

from app.service.DynamoService import DynamoService
from app.service.SimianService import SimianService


class TestSimianService(unittest.TestCase):

    async def asyncSetUp(self):
        self.service_is_simian = SimianService(['AAAA', 'TTTT', 'AGCT', 'CCGT'])

    @unittest.skip
    async def test_DeveSerUmHumano(self):
        dna = ['ACGT', 'GTAG', 'AGCT', 'CCGT']
        simian_service = await SimianService(dna)
        self.assertEqual(simian_service.is_simian(), False)

    def test_DeveSerUmSimian(self, simian_service=None):
        dna = ['AAAA', 'TTTT', 'AGCT', 'CCGT']
        with simian_service = SimianService(['AAAA', 'TTTT', 'AGCT', 'CCGT']):
            self.assertEqual(simian_service.is_simian(), True)

    @unittest.skip
    async def test_DeveSerUmSimianDnaLongo(self):
        dna = ["AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
               "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
               "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
               "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
               "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
               "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
               "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
               "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"]
        simian_service = await SimianService(dna)
        self.assertEqual(simian_service.is_simian(), True)

if __name__ == '__main__':
    unittest.main()