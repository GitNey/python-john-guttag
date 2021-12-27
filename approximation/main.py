def within_epsilon(epsilon=0.01):
  x = float(raw_input('Enter an integer to compute the square root of: '))
  #25 # constraints of search space (serves as loop termination factor)
  epsilon = float(raw_input('Specify epsilon distance to target: '))
  step = epsilon**2 # .0001 (move decimal point back 2 levels)
  numGuesses = 0 # guess counter initialized
  ans = .0 # ans initialized (serves as loop termination factor)
  # while we are not within epsilon of the target, and we are within the bounds of the search space
  # a note: search space cannot exceed a specified bound (25)
  while abs(ans**2 - x) >= epsilon and ans*ans <= x: # when x is between 0 and 1, the square root of x does not lie in this interval
  # exhaustive enumeration only works is the set of values being searched includes the answer... (that's why 0.25 won't work)
    ans += step # increment by the step
    numGuesses += 1 # increment the numGuesses counter
  print 'numGuesses =', numGuesses
  if abs(ans**2 - x) >= epsilon: # are we within epsilon?
    print 'Failed on square root of', x
  else:
    print ans, 'is close to the square root of', x

def main():
  within_epsilon()

if __name__ == '__main__':
  main()
