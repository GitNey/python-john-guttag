def get_cube():
  x = int(raw_input('Enter an integer: '))
  ans = 0 # begins at 0, but value of ans increases through loops
  # for what values of x will this program terminate? Ans: all values of x
  # since abs(x) is always positive integer there is a finite number of loops
  while ans**3 < abs(x): # ans value is tested for termination of loop
    ans += 1 # ans increases in value
  if ans**3 != abs(x):
    print x, 'is not a perfect cube'
  else:
    if x < 0:
      ans = -ans
    print 'Cube root of ' + str(x) + ' is ' + str(ans)

def just_for_fun():
  max = int(raw_input('Enter an integer: '))
  i =0
  while i < max:
    i += 1
  print i


def main():
  # the code above will print the cube root,
  # if it exists, of an integer. If the input is not
  # a perfect cube, it prints a message to that effect.
  #get_cube()
  just_for_fun()

if __name__ == '__main__':
  main()
