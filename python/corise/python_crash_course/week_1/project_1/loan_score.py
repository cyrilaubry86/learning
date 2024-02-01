def calculate_score(age, revenu, owner, debt, insurance, debt_amount=0):
  """ Calculates score based on answers given to questions.
  >>> calculate_score(55, 22000, 'yes', 'no', 'yes')
  512.5
  >>> calculate_score(17, 18000, 'no', 'no', 'no')
  -40
  >>> calculate_score(102, 80000, 'yes', 'no', 'yes')
  545.0
  >>> calculate_score(20, 50000, 'no', 'no', 'yes')
  450.0
  >>> calculate_score(55, 50000, 'yes', 'no', 'yes')
  662.5
  >>> calculate_score(55, 50000, 'yes', 'yes', 'yes', debt_amount=4000)
  462.5
  >>> calculate_score(42, 50000, 'no', 'yes', 'yes', debt_amount=62000)
  -305.0
  """
  score = 0
  if age < 20:
    score = 10
  else:
    score -= (age*2.5)
  if 0 < revenu < 5000:
    score += 0
  elif 5000 <= revenu < 10000:
    score += 5
  elif 10000 <= revenu < 30000:
    score += 50
  elif 30000 <= revenu < 50000:
    score += 100
  elif revenu >= 50000:
    score += 200
  if owner.lower() == 'yes':
    score += 300
  if owner.lower() == 'no':
    score += 0
  else:
   score += 0
  if debt == 'yes':
    score -= 100
    if debt_amount > 50000:
      score -= 500
  if debt == 'no':
    score += 100
  if insurance == 'yes':
    score += 200
  else:
    score -= 200
  return score


#########################################################################################################

#This code runs the doctests to see if they pass/fail
import doctest
doctest.run_docstring_examples(calculate_score, globals(),
    verbose=True, name="calculate_score")


#########################################################################################################

age = input("How old are you? ")
revenu = input("What is your annual revenu in USD? ")
owner = input("Do you already own any property? ")
debt = input("Are you currently already reimbursing a loan? ")
if debt == 'yes':
  debt_amount = input("how much do you have left to reimburse? ")
insurance = input("Do you want to subscribe to a loan insurance? ")

# # Once you have all the answers, send them through the calculator function
# # Note that some answers may need to be converted to numbers

#score_0 = calculate_score(80, 70000, 'yes', 'no', 'yes', debt_amount=0)

score_1 = calculate_score(int(age), int(revenu), owner, debt, insurance, debt_amount=0)

# # Now report the score to the user
##print("Your score is", score_0)

print("Your score is", score_1)


