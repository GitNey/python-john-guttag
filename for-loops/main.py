def loop_3():
  x = 4
  for j in range(x):
    for i in range(x):
      print i
      x = 2

def loop_2():
  x = 4
  for i in range(0, x):
  # range(0, x) is evaluated just before the first iteration of the
  # loop (therefore it is not revaluated because of the assingment x = 5 below.
    print i
    x = 5
    # will print 0 through 3

def loop_1():
  x = 4
  for i in range(0, x):
    print i

def find_cube_root():
  x = int(raw_input('Enter an integer: '))
  for ans in range(0, abs(x) + 1):
    if ans**3 == abs(x):
      break
  if ans**3 != abs(x):
    print x, 'is not a perfect cube'
  else:
    if x < 0:
      ans = -ans
    print 'Cube root of ' + str(x) + ' is ' + str(ans)

def loop_over_string_seq():
  t = 0
  for i in '123456789':
    t += int(i)
  print 'Total is %d' % t

def main():
  #loop_1()
  #loop_2()
  #loop_3()
  #find_cube_root()
  loop_over_string_seq()

if __name__ == '__main__':
  main()
