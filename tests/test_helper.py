import unittest
from app.helper.Helper import Helper


class TestHelper(unittest.TestCase):

    def test_generate_partition_key(self):
        expected_partition_key = '401f003daddefaa29e7ba21e77507c6f0296fc3b'
        partition_key = Helper.generate_partition_key(['AAAA', 'TTTT', 'AGCT', 'CCGT'])

        self.assertEqual(partition_key, expected_partition_key)


if __name__ == '__main__':
    unittest.main()
