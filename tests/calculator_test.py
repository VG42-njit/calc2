"""Testing the Calculator"""
from calculator.main import Calculator

def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0

def test_calculator_add():
    """Testing the Add function of the calculator"""
    #Arrange by instantiating the calc class
    calc = Calculator()
    #Act by calling the method to be tested
    calc.add_number(1,1)
    #Assert that the results are correct
    assert calc.result == 2

def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    calc.add_number(1)
    assert calc.get_result() == 1

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    calc.subtract_number(0,1)
    assert calc.get_result() == -1

def test_calculater_multiply():
    calc = Calculater()
    calc.multiply_number(1,1)
    assert calc.get_result() == 1

def test_calculater_divide():
    calc = Calculater()
    calc.divide_number(1,1)
    calc.divide_number(1,0)
    assert calc.get_result() == 1
    assert calc.divide_number == "not valid"
