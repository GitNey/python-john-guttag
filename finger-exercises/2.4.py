def get_input():
  try:
    result = raw_input('Enter 10 integers: ')
    return result
  except Exception:
    raise Exception('Invalid input. Try again.')

def task():
  i = get_input()
  print(i, type(i))
  if (type(i) == str and ' ' in i):
    inputs = [int(num) for num in i.split(' ') if int(num) % 2 != 0]
  elif (type(i) == str and ' ' not in i):
    inputs = int(i)
    if inputs % 2 != 0:
      pass
    else:
      print 'No odd numbers provided in user input.'
      return 1
  else:
    raise Exception('No inputs provided')
  if (len(inputs) > 0):
    if (len(inputs) > 9):
      print 'Just a heads up, you provided more than the specified amount of inputs but we will proceed anyways...'
    inputs.sort()
    print 'The largest odd number is: %d' % inputs.pop()
  else:
    print 'No odd numbers provided in user input.'

def main():
  # Write a program that asks user to input 10 integers, and
  # then prints the largest odd number that was entered.
  # If no odd number was entered, it should print a message to that effect.
  task()

if __name__ == '__main__':
  main()
