import unittest
from unittest.mock import Mock, MagicMock

from app.service.SimianService import SimianService


class TestSimianService(unittest.TestCase):

    def setUp(self):
        self.mock1 = SimianService.is_simian

    def tearDown(self) -> None:
        SimianService.is_simian = self.mock1

    def test_is_simian(self):
        simian_service = SimianService(self.get_dna())
        response = simian_service.is_simian()
        assert response == True

    def get_dna(self):
        return ['AAAA', 'TTTT', 'AGCT', 'CCGT']


if __name__ == '__main__':
    unittest.main()
