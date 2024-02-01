"""
Code examples of the Real Python: Functions and Loops course
"""


type(print)


def shout_and_return(input_string):
    """Prints and returns a string in uppercase."""
    loud_input = input_string.upper()
    print(loud_input)
    return loud_input


#help(shout_and_return)


n = 1
while n < 5:
    print(n)
    n = n + 1


word = "Donut"
index = 0

while index < len(word):
    print(word[index])
    index = index + 1


num = float(input("Enter a positive number: "))

while num <= 0:
    print("That's not a positive number!")
    num = float(input("Enter a positive number: "))


for n in range(1, 5):
    print(n)


for letter in "Donut":
    print(letter)


for n in range(1, 4):
    for j in range(1, 4):
        print(f"n = {n} and j = {j}")




