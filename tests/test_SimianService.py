import unittest
import boto3 

from moto import mock_dynamodb

from app.service.DynamoService import DynamoService
from app.service.SimianService import SimianService

class TestSimianService(unittest.TestCase):

    def test_DeveSerUmHumano(self):
        dna = ['ACGT', 'GTAG', 'AGCT', 'CCGT']
        simian_service = SimianService(dna)
        #self.assertEqual(simian_service.is_simian(), False)

    def test_DeveSerUmSimian(self):
        dna = ['AAAA', 'TTTT', 'AGCT', 'CCGT']
        simian_service = SimianService(dna)
        print('>>', simian_service.is_simian())
        #self.assertEqual(simian_service.is_simian(), True)

if __name__ == '__main__':
    unittest.main()