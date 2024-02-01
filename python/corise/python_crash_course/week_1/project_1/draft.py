import random


 
rand_list=[]
n = 40
for i in range(n):
    rand_list.append(random.randint(1,200))
print(rand_list)


list_ = [chr(i) for i in range(97, 123)]
print(list_)

list_2 = [chr(i) for i in range(50, 90)]
print(list_2)


n = range(1, 10)

print(n)