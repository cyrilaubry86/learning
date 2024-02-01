import random

rand_num = random.randint(1, 10000)
rand_char = chr(rand_num)

print(rand_char)


def random_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return [r, g, b]

random_rgb()




yays = ["You got it!", "Congrats!", "Well done!", "Nice one!"]

random.choice(yays)



count = 0

while True:
    rand_num = random.randint(0,10000)
    if rand_num > 10:
        print(rand_num)
        count += 1
    else:
        count += 1
        print(f"we got a small number! : {rand_num}, and the count was : {count}")
        break






import random

num_experiments = 10000

one_called = 0
two_called = 0
three_called = 0

for _ in range(num_experiments):
  random_num = random.randint(1, 3)
  if random_num == 1:
    one_called += 1
  elif random_num == 2:
    two_called += 1
  elif random_num == 3:
    three_called += 1

def report_frequency(num, call_count, total_count):
  percentage = call_count/total_count
  print(f"{num} called {call_count} times: {percentage}")

report_frequency(1, one_called, num_experiments)
report_frequency(2, two_called, num_experiments)
report_frequency(3, three_called, num_experiments)