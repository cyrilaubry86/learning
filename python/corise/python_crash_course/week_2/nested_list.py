











# def sum_grid(grid):
#     """Returns the sum of all the numbers in the given grid, a 2-D list of numbers.

#     >>> grid1 = [
#     ...     [5, 1, 6],   # 12
#     ...     [10, 4, 1],  # 15
#     ...     [8, 3, 2]    # 13
#     ... ]
#     >>> sum_grid(grid1)
#     40
#     >>> grid2 = [
#     ...     [15, 1, 6], # 22
#     ...     [10, 4, 0], # 14
#     ...     [8, 3, 2]   # 13
#     ... ]
#     >>> sum_grid(grid2)
#     49
#     """
#     # Initialize a sum to 0
#     sum = 0
#     # Iterate through the grid
#     for row in grid:
#         for e in row:
#             sum += e
#     return sum
    
    
def contains_15row(grid):
    """Takes an input of a 2-dimensional list of numbers
        and returns true if any of the rows add up to 15.

    >>> grid1 = [
    ...     [5, 1, 6],   # 12
    ...     [10, 4, 1],  # 15!!
    ...     [8, 3, 2]    # 13
    ... ]
    >>> contains_15row(grid1)
    True
    >>> grid2 = [
    ...     [15, 1, 6], # 22
    ...     [10, 4, 0], # 14
    ...     [8, 3, 2]   # 13
    ... ]
    >>> contains_15row(grid2)
    False
    """
    #true_counter =0
    row_sum = 0
    for row in grid:
        for pixel in row:
            row_sum += pixel
    print(row_sum)
    if row_sum == 15:
        #true_counter += 1
        #print(true_counter)
        return True
        
    # Iterate through the grid
    # Initialize a sum to 0
    # Iterate through the row
    # Add current value to sum
    # If sum is 15, return true
    # return false otherwise
    
     
grid1 = [
[5, 1, 6],   # 12
[10, 4, 1],  # 15!!
[8, 3, 2]    # 13
  ]

contains_15row(grid1)