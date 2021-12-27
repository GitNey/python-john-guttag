
def get_user_input():
  try:
    i = int(raw_input('Input an integer: '))
    return i
  except Exception:
    print('Invalid input. Try again')

def program():
  x = get_user_input()
  pwr = 0
  root = 1
  passed = False
  while root <= x:
    #print(root, '**', pwr)
    if (root**pwr == x):
      passed = True
      print(str(root) + ' to the power of ' + str(pwr) + ' is: ' + str(root**pwr))

    if pwr >= 6:
      root += 1
      pwr = 0
    else:
      pwr += 1
  else:
    print 'Loop terminated'
    if not passed:
      print 'The input number has no combination of root**pwr for values 1 -> 6'

def main():
  # Write a program that asks the user to input an integer
  # and prints two integers: root and pwr, such that 0 < pwr < 6
  # (for any pwr value in range 1, 2, 3, 4... 6) root**pwr is equal to the integer
  # entered by the user. If no such pair exists, print a message to that effect.
  program()

if __name__ == '__main__':
  main()
