from unittest import TestCase

from TwoSum import two_sum


class Test(TestCase):
    def test_two_sum_positive_scenario(self):
        self.assertTrue(two_sum([10, 15, 3, 7], 17))

    def test_two_sum_negative_scenario(self):
        self.assertFalse(two_sum([1, 2, 3, 4], 10))

    def test_two_sum_same_value(self):
        self.assertFalse(two_sum([1, 2], 4))

    def test_two_sum_one_element(self):
        self.assertFalse(two_sum([1], 2))

    def test_two_sum_no_element(self):
        self.assertFalse(two_sum([], 0))
