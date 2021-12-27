def is_odd(n):
  return n % 2 != 0

def parse_vars(x, y, z):
  nums = [x, y, z]
  #odds = [num for num in nums if num % 2 != 0]
  odds = [num for num in nums if is_odd(num)] # cool bro, using function calls in list comprehensions... so pythonic
  if (len(odds) > 0):
    odds.sort()
    print ('The largest odd number is:', odds.pop())
  else:
    print ('No odd numbers found')

def parse_vars_branching(x, y, z):
  if (x % 2 != 0) or (y % 2 != 0) or (z % 2 != 0):
    # code block executes if x or y or z is odd...
    # initialize the variable largest with odd number assignment so we go through each...
    if (x % 2 != 0):
      largest = x
    if (y % 2 != 0):
      largest = y
    if (z % 2 != 0):
      largest = z

    if (x % 2 != 0):
      if (x > largest):
        largest = x
    if (y % 2 != 0):
      if (y > largest):
        largest = y
    if (z % 2 != 0):
      if (z > largest):
        z = largest
    print 'The largest odd number is %d' % largest
  else:
    print 'No odd numbers found'

def main():
  # write a program that examines three variables (x, y, z)
  # and prints the largest odd number among them,
  # if none are odd, it should print a message to that effect.
  parse_vars(13, 4, 11)
  parse_vars(-13, -11, -4)
  parse_vars(2, 4, 6)
  # ----------------------------
  parse_vars_branching(13, 4, 11)
  parse_vars_branching(-13, -11, -4)
  parse_vars_branching(2, 4, 6)

if __name__ == '__main__':
  main()
