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
  guess = haystack[ haystack.index(needle[0]) ]
  guessCounter = 0
  index = 0
  while (not match):
    if guess == needle:
      match = True
    else:
      guessCounter += 1
      index = haystack.index(needle[0])
      haystack = haystack[ index :]
      try:
        guess = haystack[ haystack.index(needle[0:guessCounter])]
      except Exception:
        pass
      print 'Current guess: %s' % guess
  print 'Needle found at index: %d' % index
  print 'Number of guesses required: %d' % guessCounter

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
