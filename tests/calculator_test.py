"""Testing the Calculator"""
from calculator.main import Calculator

def test_calculator_result():
    """testing calculator result is 0"""
    calc1 = Calculator()
    assert calc1.result == 0

def test_calculator_add():
    """Testing the Add function of the calculator"""
    #Arrange by instantiating the calc class
    calc1 = Calculator()
    #Act by calling the method to be tested
    calc1.add_number(1)
    #Assert that the results are correct
    assert calc1.result == 2

def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc2 = Calculator()
    calc2.add_number(1)
    assert calc2.get_result() == 2

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc3 = Calculator()
    calc3.subtract_number(0)
    assert calc3.get_result() == -1



def test_calculator_multiply():
    calc4 = Calculator()
    calc4.multiply_number(1)
    assert calc4.get_result() == 1


