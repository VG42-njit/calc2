
class Calculator:
  #empty constructor
  def __init__(self):
    pass
  #add method - given two numbers, return the addition
  @staticmethod
  def add(x1, x2):
    return x1 + x2
  #multiply method - given two numbers, return the
  #multiplication of the two
  @staticmethod
  def multiply(x1, x2):
    return x1 * x2
  #subtract method - given two numbers, return the value
  #of first value minus the second
  @staticmethod
  def subtract(x1, x2):
    return x1 - x2
  #divide method - given two numbers, return the value
  #of first value divided by the second
  @staticmethod
  def divide(x1, x2):
    if x2 != 0:
      return x1/x2