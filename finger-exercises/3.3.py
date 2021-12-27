
def program(s = '1.23,2.4,3.123'):
  temp = ''
  sum = 0
  for i in s:
    if i != ',':
      temp += i
    else:
      sum += float(temp)
      temp = '0'
  sum += float(temp)
  print 'Sum is:', str(sum)
  # test
  print 'Sum is correct: ', 1.23 + 2.4 + 3.123

def main():
  # Let s be a string that contains a sequence of decimal numbers separated by commas
  # e.g: '1.23,2.4,3.123'.
  # Write a program that prints the total sum of the numbers in s
  program()

if __name__ == '__main__':
  main()
