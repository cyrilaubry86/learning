for num in range(1, 5):
    print(9 * num)


for n in range(1, 600, 50):
    print(n)


members = ["Pamela", "Tinu", "Brenda", "Kaya"]

print(members[0])
print(len(members))

print(len("🤷🏽‍♀️"))


scores = [80, 95, 78, 92]
total = 0
i = 0
while i < len(scores):
    score = scores[i]
    total += score
    i += 1
    
# print(total)


scores = [80, 95, 78, 92]
total = 0
for score in scores:
    total += score

letters = "(*&*^&^&%*^%$%#$^@!#$_)'][=]"
for letter in letters:
    print(ord(letter))
    
    
emoji = "🤷🏽‍♀️"
for code_point in emoji:
    print(ord(code_point))


def make_point(x, y):
  """Returns a list with the two arguments, rounded to their integer values.
  
  >>> make_point(30, 75)
  [30, 75]
  >>> make_point(-1, -2)
  [-1, -2]
  >>> make_point(12.32, 74.11)
  [12, 74]
  """
  x_int = round(x)
  y_int = round(y)
  return [x_int, y_int]

import doctest
doctest.run_docstring_examples(make_point, globals(),
    verbose=True, name="make_point")


def average_scores(scores):
  """Returns the average of the provided scores.
  
  >>> average_scores([10, 20])
  15.0
  >>> average_scores([90, 80, 70])
  80.0
  >>> average_scores([8.9, 7.2])
  8.05
  """
  # Initialize a variable to 0
  # Iterate through the scores
      # Add each score to the variable
  # Divide the variable by the number of scores
  # Return the result
  i = 0
  for score in scores:
    i += score
    result = i / len(scores)
    
  return result

import doctest
doctest.run_docstring_examples(average_scores, globals(),
    verbose=True, name="make_point")




def concatenator(items):
    """Returns a string with all the contents of the list concatenated together.

    >>> concatenator(["Super", "cali", "fragilistic", "expialidocious"])
    'Supercalifragilisticexpialidocious'
    >>> concatenator(["finger", "spitzen", "gefühl"])
    'fingerspitzengefühl'
    >>> concatenator(["none", "the", "less"])
    'nonetheless'
    """
    # Initialize a variable to empty string
    # Iterate through the list
      # Concatenate each item to the variable
    # Return the variable
    
    concatenated_string = ''
    for e in items:
        concatenated_string += e
    print(f'\'{concatenated_string}\'')
      
    concatenator(['lala', 'cyril', 'doudouti'])