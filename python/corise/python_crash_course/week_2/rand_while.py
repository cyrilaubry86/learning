import random
import time
start_time = time.time()




# rand_number = random.randint(1,1000000)
# print(rand_number)

# counter = 0
# event_count = 0
# while True:
#     rand_number = random.randint(1,1000000)
#     print(rand_number)
#     if rand_number == 42:
#         print(rand_number)
#         print('Hey, got 42 !')
#         event_count += 1
#         break
#     counter += 1
# print(f'counter is {counter}')
# print(f'the event_count is {event_count}')
# print("--- %s seconds ---" % round((time.time() - start_time), 2))


# def find_42(n):
#     counter = 0
#     while True:
#         rand_number = random.randint(0, n)
#         #print(rand_number)
#         if rand_number == 42:
#             #print(rand_number)
#             #print('Hey, got 42 !')
#             break
#         counter += 1
#     print(counter)
#     #return counter
#     #print(f'counter is {counter}')
#     #print("--- %s seconds ---" % round((time.time() - start_time), 2))



# upper_bound = 4
# n = 1000000
# runtimes = 0
# for i in range(1, upper_bound):
#     find_42(n)
#     runtime = round((time.time() - start_time), 2)
#     runtimes += runtime
# avg_runtime = round(runtime / (upper_bound - 1), 2)
# print(f'{avg_runtime} seconds')
    
    
    
    
    
##########################################
def find_number(n, number):
    counter = 0
    while True:
        rand_number = random.randint(0, n)
        #print(rand_number)
        if rand_number == number:
            #print(rand_number)
            #print('Hey, got 42 !')
            break
        counter += 1
    #print(counter)
    #print(counter_list)
    return counter
    #print(f'counter is {counter}')
    #print("--- %s seconds ---" % round((time.time() - start_time), 2))


def run_number(n, upper_bound, number):
    counter_list = []
    runtimes = 0
    for i in range(1, upper_bound):
        find_number(n, number)
        runtime = round((time.time() - start_time), 2)
        runtimes += runtime
        counter_list.append(find_number(n, number))
    avg_runtime = round(runtime / (upper_bound - 1), 2)
    avg_counter = round(sum(counter_list) / len(counter_list), 2)
    print(f'We ran {upper_bound} iterations in order to find number {number} in a random generated numbers, in a range of (1, {n})')
    print(f'Average runtime is : {avg_runtime} seconds')
    #print(counter_list)
    print(f'Average counter is : {avg_counter}')
    
run_number(1000000, 10, 42)