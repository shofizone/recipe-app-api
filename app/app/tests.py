from django.test import TestCase

from app.calc import add, subtuct


class CalcTest(TestCase):
    def test_add_number(self):
        self.assertEqual(add(3, 2), 5)

    def test_subtruct_number(self):
        """ Testing subtrut """
        self.assertEqual(subtuct(5, 2), 3)
