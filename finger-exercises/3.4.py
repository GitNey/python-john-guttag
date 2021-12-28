def binary_to_dec(binary):
  sum = 0
  idx = 0
  r = range(len(binary))
  r.reverse()
  for i in r:
    #print 'power:', 2**i
    #print 'idx:', i
    #print 'char at idx:', reverse_str(binary)[i]
    if reverse_str(binary)[i] == '1':
      sum += 2**i # add base 2 value at index
    #print 'sum:', sum
    #print '-' * 15
  return sum

def reverse_str(s):
  return s[::-1]

def bin_to_decimal(n):
  result = binary_to_dec('10011')
  print str(n), 'is:', result

  print 'Tests:'
  print '10011 is 19?', binary_to_dec('10011') == 19
  print '00101101 is 45?', binary_to_dec('00101101') == 45
  print '01010101110101 is 5493?', binary_to_dec('01010101110101') == 5493

def main():
  # what is the decimal equivalent of the binary number 10011?
  bin_to_decimal(10011)


if __name__ == '__main__':
  main()
