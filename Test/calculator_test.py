import pytest
from app.calc import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_correct(self):
        assert self.calc.multiply(self, 7, 8) == 56

    def test_division_correct(self):
        assert self.calc.division(self, 256, 16) == 16

    def test_subtraction_correct(self):
        assert self.calc.subtraction(self, 23, 11) == 12

    def test_adding_correct(self):
        assert self.calc.adding(self, 13, 17) == 30

    def teardown(self):
        print('Выполнение метода teardown')
