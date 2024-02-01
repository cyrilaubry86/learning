# def count_evens(start, end):
#     """
#     Counts the number of even numbers between a given start number and given end number.
#     Count should include the start or end if they are even.
#     >>> count_evens(2, 2)
#     1
#     >>> count_evens(-2, 52)
#     28
#     >>> count_evens(237, 500)
#     132
#     """
#     current_number = start
#     num_even = 0
#     while current_number <= end:
#         if current_number % 2 == 0:
#             num_even += 1
#         current_number += 1
#     return num_even

# import doctest
# doctest.run_docstring_examples(count_evens, globals(),
#     verbose=True, name="count_evens")



# def count_multiples(start, end, divisor):
#     """
#     Counts the number of multiples of divisor between the start and end numbers.
#     It should include the start or end if they are a multiple.
     
#     >>> count_multiples(2, 2, 1)       # 2 is a multiple of 1
#     1
#     >>> count_multiples(2, 2, 2)       # 2 is a multiple of 2
#     1
#     >>> count_multiples(2, 2, 3)       # 2 is not a multiple of 3
#     0
#     >>> count_multiples(1, 12, 3)      # 3, 6, 9, 12
#     4
#     >>> count_multiples(237, 500, 10)
#     27
#     """
#     current_number = start
#     num_even = 0
#     while current_number <= end:
#         if current_number % divisor == 0:
#             num_even += 1
#         current_number += 1
#     return num_even




# def sum_multiples(start, end, divisor):
#     """Returns the sum of the multiples of a given divisor between start and end.
#     If the start or end numbers are multiples, they should be included in the sum.

#     >>> sum_multiples(1, 12, 4)
#     24
#     >>> sum_multiples(1, 12, 13)
#     0
#     >>> sum_multiples(2, 2, 2)
#     2
#     >>> sum_multiples(2, 2, 3)
#     0
#     >>> sum_multiples(23, 81, 13)
#     260
#     """
#     current_number = start
#     sum_divisor = 0
#     while current_number <= end:
#         if current_number % divisor == 0:
#             sum_divisor += current_number
#         current_number += 1
#     return sum_divisor


# import doctest
# doctest.run_docstring_examples(sum_multiples, globals(),
#     verbose=True, name="num_even")



def product_of_numbers(end):
    """Returns the product of all the numbers from 1 to the end number,
    including the end number.

    >>> product_of_numbers(1)
    1
    >>> product_of_numbers(2)
    2
    >>> product_of_numbers(3)
    6
    >>> product_of_numbers(10)
    3628800
    """
    result = 1
    counter = 1
    while counter <= end:
        result *= counter
        counter += 1
    return result

import doctest
doctest.run_docstring_examples(product_of_numbers, globals(),
    verbose=True, name="num_even")