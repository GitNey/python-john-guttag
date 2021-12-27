def integer_division():
  # i//j is integer division. For example, the value of 6//2 is the int 3
  # the value of 6//4 is int 1. The value is 1 because integer division
  # returns the quotient and ignores the remainder of the division operation value.
  print(6//2, type(6//2) == int, 6//2 == 3) # True, True...
  print(6//4, type(6//4) == int, 6//4 == 1) # True, True...

def addition():
  # i+j is the sum of i and j. If i and j are both type int, result is type int
  # if either i or j is a float type, the result becomes a float type.
  i = int(3)
  j = int(4)
  print(i + j, type(i + j) == int) # True...
  i = float(3)
  print(i + j, type(i + j) == float) # True...

def subtraction():
  # i-j is i minus j. If i and j are both ints, the result is an int. If either
  # of them is a float, the result is a float type.
  i = int(2)
  j = int(1)
  print(i - j, type(i - j) == int) # True...
  i = float(2)
  print(i - j, type(i - j) == float) # True...

def multiplication():
  # i*j is the product of i and j. If i and j are both ints, the result is an int.
  # if either of them is a float, the result is float.
  i = int(3)
  j = int(1)
  print(i * j, type(i * j) == int) # True...
  i = float(3)
  print(i * j, type(i * j) == float) # True...

def division():
  # in python2.7 i/j is i divided by j.
  # when the operands are both of type int, the result is of type int, otherwise of type float.
  # in this code (python 2.7 code) we write / to divide float by float.
  # in this code (python 2.7 code) we write // to divide int by int.
  # python 3 makes divide operation return float.
  print('6 / 4 =', 6/4, type(6/4) == int) # True...
  print('6.0/4 =', 6.0/4, type(6.0/4) == float) # True...

def modulo_operation():
  # i%j is the remainder when the int i is divided by int j. i modulo j.
  print('4 % 3 =', 1, type(4%3) == int) # True...
  print(type(4.0%3) == float) # True...

def exponentiation():
  # i**j is i to the power of j
  # always returns type float if either is of type float else int.
  i = 2
  j = 3
  print(i**j, type(i**j) == int) # True...

def main():
  lineSeparator = 20 * '-'
  addition()
  print(lineSeparator)
  subtraction()
  print(lineSeparator)
  multiplication()
  print(lineSeparator)
  integer_division()
  print(lineSeparator)
  division()
  print(lineSeparator)
  modulo_operation()
  print(lineSeparator)
  exponentiation()

if (__name__ == '__main__'):
  main()
