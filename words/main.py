import string

def read_file(name='words.txt'):
  file = open(name, 'r')
  lines = file.readlines()
  file.close()
  return lines

def remove_newline(word):
  return word.strip()

def bisection_search(needle, haystack):
  map = dict(zip(string.ascii_lowercase, range(1, 27)))
  match = False
  needle == haystack[ haystack.index(needle) ]
  needleIndex = haystack.index(needle)
  guessIndex = (len(haystack) - 1) / 2
  guessCounter = 0
  index = 0
  while (not match):
    guess = haystack[ guessIndex ]

    # look left or right if only two items remain in search space.
    if len(haystack) == 2 and guess != needle and guessIndex == 0:
        guessIndex += 1
        guess = haystack[guessIndex]
    elif len(haystack) == 2 and guess != needle and guessIndex == 1:
        guessIndex -= 1
        guess = haystack[guessIndex]

    if guess == needle:
      match = True
      print 'Correct guess:', guess
    else:
      guessCounter += 1
      a = haystack[0:guessIndex]
      b = haystack[guessIndex:]

      if needle in a:
        guessIndex = (len(a) - 1) / 2
        haystack = a
      else:
        guessIndex = (len(a) - 1) / 2
        haystack = b

      print 'Current guess: %s' % guess
      print 'Current haystack size: %d' % len(haystack)
      print 'Haystack:', haystack
      print '\n\n\n\n'
  print 'Needle found at index: %d' % guessIndex
  print 'Number of guesses required: %d' % guessCounter
  return needle

def search_exhaustively(needle, haystack):
  match = False
  index = 0
  guessCounter = 0
  while (not match):
    guess = haystack[index]
    guessCounter += 1
    if needle == guess:
      match = True
      print 'Needle found at index: %d' % index
      print 'Number of guesses required: %d' % guessCounter
    else:
      index += 1
  return needle

def main():
  words_sanitized = [remove_newline(word).lower() for word in read_file()]
  search_exhaustively('zebra', words_sanitized)
  bisection_search('zebra', words_sanitized)

if __name__ == '__main__':
  main()
