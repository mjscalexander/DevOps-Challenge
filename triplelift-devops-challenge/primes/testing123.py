import unittest
from find_optimus import is_prime
from finding_composites import is_composites
from finding_composites import get_total_composites

# These are test written to test the functionaltiy of the prime
# and composite scripts

class PrimeandCompositeTest(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(3))

    def test_is_not_prime(self):
        self.assertFalse(is_prime(4))

    def test_prime_and_composites_not_zero_or_one(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_composites(0))


    def test_negative_integers(self):
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_composites(-4))
        self.assertFalse(is_composites(-1))

    def test_is_composite(self):
        self.assertTrue(is_composites(4))

    def test_is_not_composite(self):
        self.assertFalse(is_composites(3))

    def test_get_total_composite(self):
        self.assertEqual(get_total_composites(100000), '90407')



if __name__ == '__main__':
    unittest.main()





