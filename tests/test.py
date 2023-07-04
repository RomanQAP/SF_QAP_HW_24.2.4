from app.calc import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    # Позитивный тест №1
    def test_multiply_success(self):
        assert self.calc.multiply(self, 5, 10) == 50

    # Позитивный тест №2
    def test_division_succes(self):
        assert self.calc.division(self, 100, 50) == 2

    # Позитивный тест №2
    def test_subtraction_succes(self):
        assert self.calc.subtraction(self, 49, 9) == 40

    # Позитивный тест №4
    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def teardown(self):
        print('Тест пройден')
