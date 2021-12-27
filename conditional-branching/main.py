def conditional_branching(x):
  if x % 2 == 0:
    print '%d is an even value' % x
  else:
    print '%d is an odd value' % x
  print 'Done with conditional branching computation.'

def main():
  conditional_branching(12)
  conditional_branching(3)

if __name__ == '__main__':
  main()
