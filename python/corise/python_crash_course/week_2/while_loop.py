



# n = 1
# total = 0

# while n <= 5:
#     total += (2 * n)
#     n += 1
#     print(total)
    
    
    
def total_multiples(up_to):
    n = 1
    total = 0

    while n <= up_to:
        total += (5 * n)
        n += 1
    return total


print(total_multiples(5))