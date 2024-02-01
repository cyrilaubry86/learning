




# def add_to_sequence(sequence):    
#     """
#     >>> nums = [1, 2, 3]
#     >>> add_to_sequence(nums)
#     >>> nums
#     [1, 2, 3, 4]
#     >>> nums2 = [26, 27]
#     >>> add_to_sequence(nums2)
#     >>> nums2
#     [26, 27, 28]
#     """
#     final_item = int(sequence[-1]) +1 
#     return sequence.append(final_item)





# import math
# def malcolm_in_middle(sequence):
#     """
#     >>> kids = ['jamie', 'dewey', 'reese', 'francis']
#     >>> malcolm_in_middle(kids)
#     >>> kids
#     ['jamie', 'dewey', 'malcolm', 'reese', 'francis']
#     >>> kids2 = ['hunter', 'pamela', 'oliver']
#     >>> malcolm_in_middle(kids2)
#     >>> kids2
#     ['hunter', 'pamela', 'malcolm', 'oliver']
#     """
#     ind = math.ceil(len(sequence) / 2)
#     sequence.insert(ind, 'malcolm')

# import doctest
# doctest.run_docstring_examples(malcolm_in_middle, globals(),
#     verbose=True)





# sequence = [-1, -4]
# new_list = []

# for e in sequence:
#     new_list.append(e*2)
# print(new_list)



# def double_time(sequence):
#     new_list = []
#     for e in sequence:
#         new_list.append(e*2)
#     return new_list




# sequence = [1, 2, 3]

# print(double_time(sequence))




# def double_time(sequence):
#     """
#     >>> nums = [1, 2, 3]
#     >>> double_time(nums)
#     >>> nums
#     [2, 4, 6]
#     >>> nums2 = [-1, -4]
#     >>> double_time(nums2)
#     >>> nums2
#     [-2, -8]
#     """
#     new_list = []
#     n = len(sequence)
#     while e in sequence:
#         new_list.append(e*2)
#     return new_list






def double_time(sequence):
    """
    >>> nums = [1, 2, 3]
    >>> double_time(nums)
    >>> nums
    [2, 4, 6]
    >>> nums2 = [-1, -4]
    >>> double_time(nums2)
    >>> nums2
    [-2, -8]
    """
    # how to double the value of each element in the sequence
    
    new_list = []
    i = 0
    while i < len(sequence):
        new_list.append(sequence[i] * 2)
        i += 1
    return new_list


import doctest
doctest.run_docstring_examples(double_time, globals(),
    verbose=True)

# sequence = [1, 2, 3]
# double_time(sequence)





# 2nd
def double_time(sequence):
    """
    >>> nums = [1, 2, 3]
    >>> double_time(nums)
    >>> nums
    [2, 4, 6]
    >>> nums2 = [-1, -4]
    >>> double_time(nums2)
    >>> nums2
    [-2, -8]
    """
    # how to double the value of each element in the sequence
    
    i = 0
    while i < len(sequence):
        sequence[i] = sequence[i] * 2
        i += 1
    return sequence


import doctest
doctest.run_docstring_examples(double_time, globals(),
    verbose=True)

# sequence = [1, 2, 3]
# double_time(sequence)