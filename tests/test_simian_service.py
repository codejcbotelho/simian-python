import unittest
from app.service.SimianService import SimianService


class TestSimianService(unittest.TestCase):

    def test_is_simian(self):
        simian_service = SimianService(TestSimianService.get_dna())
        response = simian_service.is_simian()
        self.assertEqual(response, True)

    @classmethod
    def get_dna(cls):
        return ['AAAA', 'TTTT', 'AGCT', 'CCGT']


if __name__ == '__main__':
    unittest.main()
