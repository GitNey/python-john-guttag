def iteration_example():
  x = 3 # bind the variable x to the int 3
  ans = 0
  itersLeft = abs(x) # use absolute values to ensure itersLeft is never a negative value
  while (itersLeft != 0): # square x using repetetive addition
    # when considering terminating values and what itersLeft test could evaluate to
    # consider itersLeft becomes equal to -1. Program will never execute, infinite loop
    ans += abs(x) # see absolute values prevent infinite loop
    itersLeft -= 1
  # for values above 0 the loop body will execute, program
  # termination occurs when itersLeft is 0
  print str(x) + '*' + str(x) + ' = ' + str(ans)

def main():
  iteration_example()


if __name__ == '__main__':
  main()
