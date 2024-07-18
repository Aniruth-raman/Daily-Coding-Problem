from unittest import TestCase

from ProductExceptCurrent import product_except_current


class Test(TestCase):
    def test_product_except_current_positive_scenario_1(self):
        self.assertEqual([120, 60, 40, 30, 24], product_except_current([1, 2, 3, 4, 5]))

    def test_product_except_current_positive_scenario_2(self):
        self.assertEqual([2, 3, 6], product_except_current([3, 2, 1]))