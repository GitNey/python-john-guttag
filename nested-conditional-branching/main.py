

def nested_conditional_branching(x):
  if x % 2 == 0: # is x perfectly divisible by 2?
    if x % 3 == 0: # is x perfectly divisible by 3?
      print '%d is divisible by 2 and by 3' % x
    else:
      print '%d is divisible by 2 but not by 3' % x
  elif x % 3 == 0:
    print '%d is divisible by 3 and not by 2' % x

def main():
  nested_conditional_branching(12)
  nested_conditional_branching(4)
  nested_conditional_branching(9)

if __name__ == '__main__':
  main()
