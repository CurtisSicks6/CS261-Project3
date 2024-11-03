# Name: Curtis Sicks
# OSU Email: sicksc@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 1 (Python Fundamentals Review)
# Due Date: 10/21/2024
# Description: Problem set of 10 functions to be used in conjunction
# with members of the StaticArray class.


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> tuple[int, int]:
    """Take a one-dimensional array and returns a tuple with minimum and maximum values of the array."""

    # Initialize min and max values to first element of the array

    min_value = arr.get(0)
    max_value = arr.get(0)

    # Iterate through the array once.
    for x in range(1, arr.length()):
        compared_value = arr.get(x)
        if compared_value < min_value:
            min_value = compared_value
        if compared_value > max_value:
            max_value = compared_value
    return min_value, max_value

    # Checking min and max is O(1) complexity on each element
    # Has to go through n-1 iterations, where n is number of elements in array
    # O(n-1) simplifies to O(n) complexity
    pass

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """Takes a static array object and returns a new static array object with fizzbuzz logic built into it."""

    # Create a new array so the input array isn't being changed. Make it match input array length
    new_array = StaticArray(arr.length())

    # Apply fizzbuzz logic.
    for x in range(arr.length()):
        value = arr.get(x)

        if value % 3 == 0 and value % 5 == 0:
            new_array.set(x, 'fizzbuzz')
        elif value % 3 == 0:
            new_array.set(x, 'fizz')
        elif value % 5 == 0:
            new_array.set(x, 'buzz')
        else:
            new_array.set(x, value)

    return new_array

    # Iterate through the array once.
    # Checking each element and updating it is O(1) complexity
    # Has to go through n iterations, where n is number of elements in array. O(n) complexity
    pass


# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """ Reverses the order of elements within the input array."""

    # Create start and end points for the array
    left = 0
    right = arr.length() - 1

    while left < right:

        # Hold the left index value as its own variable. We need it because the left value is being reversed first.
        left_holder = arr.get(left)

        # Execute the reversal
        arr.set(left, arr.get(right))
        arr.set(right, left_holder)

        # Advance the start and end points
        left = left + 1
        right = right - 1

    # Iterate through the array once.
    # Checking each element and updating it is O(1) complexity
    # Has to go through n iterations, where n is number of elements in array. O(n) complexity
    pass


# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """ Returns a new StaticArray with the position of the elements in the array having been shifted left or right
    depending on the positive or negative integer passed to the function.
    """
    # Create a new empty array that is the same length as the input array.
    length = arr.length()
    rotated_array = StaticArray(length)

    # Step values that are greater than the length of the array will loop over themselves.
    # We're only concerned with the remainder of the steps divided by the length.
    effective_steps = steps % length

    # Run through elements in the loop and rotate their positions. Use modulo to wrap elements back around.
    for x in range(arr.length()):
        rotated_index = (x + effective_steps) % length
        rotated_array.set(rotated_index, arr.get(x))
    return rotated_array

    # Iterate through the array once.
    # Checking each element and updating it is O(1) complexity
    # Has to go through n iterations, where n is number of elements in array. O(n) complexity

    pass


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """ Takes two integers and returns a StaticArray Object with all consecutive integers
    between them sorted. Includes start and end integers
    """
    # Determine length of the array we will create.
    length = abs(end-start) + 1

    # Create the array.
    range_array = StaticArray(length)

    # Iterate through the length of the array and set consecutive integers in place.
    for x in range(length):
        if start >= end:
            range_array.set(x, start - x)
        else:
            range_array.set(x, start + x)

    return range_array

    # Iterate through the array once.
    # Checking each element and updating it is O(1) complexity
    # Has to go through n iterations, where n is the range of the array. O(n) complexity

    pass

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------


def is_sorted(arr: StaticArray) -> int:
    """ Determines if an array is sorted in ascending or descending order. If neither is true, return 0"""

    length = arr.length()

    # Edge case for arrays of length 1.
    if length == 1:
        return 1

    # Set initial boolean conditions for ascending and descending.
    ascending = True
    descending = True

    # Iterate through the array and update ascending and descending boolean values
    for x in range(0, length - 1):
        if arr.get(x + 1) > arr.get(x):
            descending = False
        elif arr.get(x + 1) < arr.get(x):
            ascending = False

        # Edge Case: Duplicate consecutive elements result in false boolean values
        else:
            ascending = False
            descending = False

    if not ascending and not descending:
        return 0

    if ascending:
        return 1
    if descending:
        return -1

    # Iterate through the array once.
    # Checking each element and updating it is O(1) complexity
    # Has to go through n-1 iterations, where n is the range of the array. O(n) complexity

    pass

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------


def find_mode(arr: StaticArray) -> tuple[object, int]:
    """ Takes Staticarray object that is sorted in either non-descending or non-ascending order
    and returns the mode and its frequency. If there is more than one mode, the one that occurs first
    is selected.
    """

    length = arr.length()

    # Edge case for arrays of length 1.
    if length == 1:
        return arr.get(0), 1

    # Initialize variables for mode and frequency
    mode = arr.get(0)
    modes_frequency = 1

    current_element_count = 1

    # Iterate through the array
    for x in range(1, length):
        if arr.get(x) == arr.get(x - 1):
            current_element_count += 1
        else:
            if current_element_count > modes_frequency:
                mode = arr.get(x - 1)
                modes_frequency = current_element_count
            current_element_count = 1

    # Edge case is the last element of the array is the mode
    if current_element_count > modes_frequency:
        mode = arr.get(length - 1)
        modes_frequency = current_element_count

    # Iterate through the array once.
    # Checking each element and updating it is O(1) complexity
    # Has to go through n-1 iterations, where n is the range of the array. O(n) complexity

    return mode, modes_frequency

    pass

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------


def remove_duplicates(arr: StaticArray) -> StaticArray:
    """ Takes a sorted StaticArray, either non-ascending/non-descending,
    and returns a new StaticArray with all duplicate values removed.
    """

    length = arr.length()

    # Edge case if array length is 1
    if length == 1:
        new_array = StaticArray(length)
        new_array.set(0, arr.get(0))
        return new_array

    # Initialize counter to detect unique elements. First element is always unique.
    unique_count = 1

    # Iterate through loop to find number of unique elements
    for x in range(1, length):
        if arr.get(x) != arr.get(x - 1):
            unique_count += 1

    # Create a new array that it the length on the unique element count.
    new_array = StaticArray(unique_count)

    # Copy only new elements into the new array. First element is always unique.
    new_array.set(0, arr.get(0))
    index = 1

    for x in range(1, length):
        if arr.get(x) != arr.get(x - 1):
            new_array.set(index, arr.get(x))
            index += 1

    return new_array

    # Iterate through the array once to check for unique elements
    # Iterate through the array again to copy those elements into a new array
    # Both tasks complexities are O(1) complexity.
    # Has to go through 2n iterations, where n is the range of the array. Simplifies to O(n) complexity

    pass


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------


def count_sort(arr: StaticArray) -> StaticArray:
    """Receives a StaticArray and returns a
    new StaticArray with the same content sorted in non-ascending order.
    """

    length = arr.length()
    new_array = StaticArray(length)

    # Edge case if array length is 1
    if length == 1:
        new_array.set(0, arr.get(0))
        return new_array

    minimum_value = arr.get(0)
    maximum_value = arr.get(0)

    # Find minimum and max values of the original array
    for x in range(1, length):
        if arr.get(x) > maximum_value:
            maximum_value = arr.get(x)
        if arr.get(x) < minimum_value:
            minimum_value = arr.get(x)

    # Determine the range of the elements with the array and create a count array
    # to keep track of how frequently those elements appear. + 1 to include max value.
    range_size = maximum_value - minimum_value + 1
    count_array = StaticArray(range_size)

    # Initialize count array
    for x in range(range_size):
        count_array.set(x, 0)

    # Fill out the count array
    for x in range(length):
        count_value = arr.get(x) - minimum_value
        count_array.set(count_value, count_array.get(count_value) + 1)

    # Example: StaticArray [-5, 3, 5, 4] Should result in a count_array of
    # [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]

    # Build the new array in non-ascending order using the count array
    index = 0

    for x in range(range_size - 1, -1, -1):
        original_value = x + minimum_value
        frequency = count_array.get(x)

        for y in range(frequency):
            new_array.set(index, original_value)
            index += 1

    return new_array

    # Iterate through the array once to determine min and max values
    # Iterate through the range size to initialize the count array
    # Iterate through the array again to fill out a count array
    # Iterate over count array to create new array.
    # O(k) complexity for range of the array
    # O(4n+k) complexity simplifies to O(n+k)

    pass


# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------


def sorted_squares(arr: StaticArray) -> StaticArray:
    """ Takes a sorted StaticArray object and returns a new array with squares of the elements
    in the original array in non-descending order.
    """
    length = arr.length()
    new_array = StaticArray(length)

    # Initialize start points for start and end of index to compare positive and negative values against each other
    left_index = 0
    right_index = length - 1
    building_index = length - 1  # Use this index to build new_array starting from the end of the array

    # Iterate through the array and compare squares at the left and right points
    while left_index <= right_index:
        left_index_square = arr.get(left_index) ** 2
        right_index_square = arr.get(right_index) ** 2

        # Build the new array
        if left_index_square > right_index_square:
            new_array.set(building_index, left_index_square)
            left_index += 1
        else:
            new_array.set(building_index, right_index_square)
            right_index -= 1

        # Shift building index
        building_index -= 1

    return new_array

    # Iterate through the array once comparing squares
    # Tasks complexities are O(1).
    # Has to go through n iterations, where n is the range of the array. O(n) complexity

    pass
