chain = {"START_OF_SENTENCE": []}

def wordify_sentence(sentence):
  """ Splits a sentence into words (space-separated),
  stripping off any periods at the end and lowercasing all the words.
  Leading, trailing, and extra whitespace should also be stripped.

  >>> wordify_sentence('Money burns a hole in your pocket.')
  ['money', 'burns', 'a', 'hole', 'in', 'your', 'pocket']
  >>> wordify_sentence(' Miss Jerry\\n ')
  ['miss', 'jerry']
  >>> wordify_sentence('The plums\\r\\n\\r\\n were so ripe.')
  ['the', 'plums', 'were', 'so', 'ripe']
  """
  list = sentence.split()
  list_2 = []
  for word in list:
    word_stripped = word.strip()
    word_lower = word_stripped.lower()
    list_2.append(word_lower)
    if '.' in word_lower:
      word_2 = word[:-1]
      list_2[-1] = word_2
  return list_2




def add_sentence(chain, sentence):
  """
  >>> test_chain = {'START_OF_SENTENCE': []}
  >>> add_sentence(test_chain, 'I am happy')
  >>> test_chain
  {'START_OF_SENTENCE': ['i'], 'i': ['am'], 'am': ['happy'], 'happy': ['END_OF_SENTENCE']}
  >>> add_sentence(test_chain, 'I am')
  >>> test_chain
  {'START_OF_SENTENCE': ['i', 'i'], 'i': ['am', 'am'], 'am': ['happy', 'END_OF_SENTENCE'], 'happy': ['END_OF_SENTENCE']}
  """
  # Split the sentence into a list of words
  words = wordify_sentence(sentence)

  # Loop through each word in the list
  # (Using a while loop gives you a way to know
  # if the word is the first or the last)
  #chain = {}
  i = 0

  while i < len(words):
    word = words[i]
    # Handle case of first word in sentence
    if word == words[0]:
      word = chain['START_OF_SENTENCE']


    # If word isn't in chain yet, add it as a key
    if word not in chain:
      chain[word] = []

    # Now figure out what word to add to
    # the list of values for this word

    # First, handle case of last word in sentence
    if word == words[-1] :
      word = chain['END_OF_SENTENCE']

    # Otherwise, handle case of a word that has a word after
    else:
      chain[word].append(word)

    i += 1
    print(chain)
    return chain
  
  
  add_sentence(chain, 'I am happy')