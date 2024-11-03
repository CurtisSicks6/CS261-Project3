# Name: Curtis Sicks
# OSU Email: sicksc@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: 10/28/24
# Description: A completed list of functions used to manipulate and traverse a dynamic array and Bag ADT class


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        Resizes the capacity of the array based on the positive integer passed to it.
        New capacity integer cannot be negative or less than size of current array.
        """

        # Only proceed if the integer passed is greater than current capacity.
        if new_capacity <= 0 or new_capacity < self._size:
            return

        # Create new array
        resized_array = StaticArray(new_capacity)

        # Populate the new array with the data from the original array.
        for x in range(self._size):
            resized_array[x] = self._data[x]

        # Update original arrays data and capacity
        self._data = resized_array
        self._capacity = new_capacity

        pass

    def append(self, value: object) -> None:
        """
        Adds the new value to the end of the dynamic array. If the array is full it doubles the current capacity,
        and then adds the value to the array.
        """

        # Double the array capacity is the array is full of elements
        if self._size == self._capacity:
            self.resize(2 * self._capacity)

        # Add new data value to end of the array and adjust the size of the array.
        self._data[self._size] = value
        self._size += 1

        pass

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts the given value at the identified index, and raises an DynamicArrayException Error if
        provided index is out of bounds.
        """

        # Handle out of bounds indices
        if index < 0 or index > self._size:
            raise DynamicArrayException("Index is out of bounds")

        # Double array capacity as needed
        if self._size == self._capacity:
            self.resize(2 * self._capacity)

        # Shift all elements starting from passed index to the right 1 position
        for x in range(self._size, index, -1):
            self._data[x] = self._data[x - 1]

        # Insert new data element at passed index
        self._data[index] = value
        self._size += 1

        pass

    def remove_at_index(self, index: int) -> None:
        """
        Removes element in the specified index. Raises an DynamicArrayException Error if
        provided index is out of bounds. If the capacity of the array is greater than 4 times
        the number of elements, reduce array size to twice the number of elements. Capacity reduction cannot
        be less than 10 elements.
        """

        # Handle out of bounds indices
        if index < 0 or index >= self._size:
            raise DynamicArrayException("Index is out of bounds")

        # Reduce array size if conditions are met. Array can not have less than 10 elements
        if self._size < self._capacity / 4 and self._capacity > 10:
            reduced_capacity = max(10, 2 * self._size)
            self.resize(reduced_capacity)

        # Overwrite element in the specified index and shift the elements left to fill the gap
        for x in range(index, self._size - 1):
            self._data[x] = self._data[x + 1]

        # Update size of the array
        self._size -= 1

        pass

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        Returns a new Dynamic array object that contains the requested number of
        elements from the original array, starting with the element located at the requested start
        index. Raises a DynamicArrayException if start index or size is invalid, or there aren't
        enough elements between the start index and end of the array to make the slice.
        """
        # Handle various invalid requests
        if start_index < 0 or start_index >= self._size:
            raise DynamicArrayException("Start index is invalid")
        if size < 0:
            raise DynamicArrayException('Size cannot be negative')
        if start_index + size > self._size:
            raise DynamicArrayException('Requested slice is too large given the original array size')

        # Create the new array
        new_array = DynamicArray()

        # Iterate through the passed size, appending the new array starting from the start index
        for x in range(size):
            new_array.append(self._data[start_index + x])

        return new_array

        pass

    def map(self, map_func) -> "DynamicArray":
        """
        Applies a specified map function to the elements of a Dynamic Array. A new array with the
        outputs of this mapped function is returned
        """
        # Create new array
        new_array = DynamicArray()

        # Iterate through array, applying the map function and populating new array with the outputs
        for x in range(self._size):
            new_array.append(map_func(self._data[x]))

        return new_array

        pass

    def filter(self, filter_func) -> "DynamicArray":
        """
        Creates a new dynamic array populated only with those elements from the
        original array for which filter_func returns True.
        """

        # Create new array
        new_array = DynamicArray()

        # Iterate through elements of the array, adding only those elements that
        # satisfy the filter function to the new array
        for x in range(self._size):
            if filter_func(self._data[x]):
                new_array.append(self._data[x])

        return new_array

        pass

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Applies the reduce function to all elements of the array and returns the resulting value.
        It takes an optional initializer parameter. If this parameter is not
        provided, the first value in the array is used as the initializer. If the dynamic array is empty,
        the method returns the value of the initializer (or None, if one was not provided).
        """

        # If array is empty, return initializer.
        if self._size == 0:
            return initializer

        # Determine the starting index for the loop to iterate through
        if initializer is not None:
            start_index = 0
        else:
            start_index = 1

        # Determine the starting value for the reduction function.
        if initializer is not None:
            result = initializer
        else:
            result = self._data[0]

        # Iterate through the array and apply the reduction function to the elements.
        for x in range(start_index, self._size):
            result = reduce_func(result, self._data[x])

        return result
        pass


def chunk(arr: DynamicArray) -> "DynamicArray":
    """
    Receives a DynamicArray of values and “chunks” it into an array of arrays, with each array consisting of a
    non-descending subsequences of values. It returns a DynamicArray, with each index of that
    array consisting of a DynamicArray containing one of the subsequences
    """
    # Create new array to hold non-descending subsequences (Each index value is its own Dynamic array)
    new_array = DynamicArray()

    # Edge case if passed array is empty
    if arr.length() == 0:
        return new_array

    # Create chunk dynamic array to store first subsequence. Add the first element to it
    chunk = DynamicArray()
    chunk.append(arr[0])

    # Iterate through Dynamic array and create subsequences
    for x in range(1, arr.length()):
        if arr[x] >= arr[x - 1]:
            chunk.append(arr[x])  # Build sequence is current element is greater or equal to preceding element
        else:
            new_array.append(chunk)  # End array and it to new_array
            chunk = DynamicArray()    # Start new chunk
            chunk.append(arr[x])    # Add first element to new array

    # Add final subsequence to chunk 
    new_array.append(chunk)

    return new_array

    # Run through the elements in the array once. O(N) complexity

    pass


def find_mode(arr: DynamicArray) -> tuple[DynamicArray, int]:
    """
    Takes a sorted (either non-ascending or non-descending) array and returns a tuple containing
    a DynamicArray with the mode(s) and an integer representing the highest frequency.
    """

    # Initialize new array and trackers for frequency
    mode_array = DynamicArray()
    highest_frequency = 0
    current_value = arr[0]
    current_value_frequency = 1

    # Iterate through the array to find mode(s) and adjust frequency
    for x in range(1, arr.length()):
        if arr[x] == current_value:
            current_value_frequency += 1
        else:
            if current_value_frequency > highest_frequency:
                highest_frequency = current_value_frequency
                mode_array = DynamicArray()  # Reset the mode array to only contain the highest occurring element(s)
                mode_array.append(current_value)
            elif current_value_frequency == highest_frequency:  # Check for multiple modes
                mode_array.append(current_value)

            current_value = arr[x]
            current_value_frequency = 1

    # Run one final check for final sequence of elements
    if current_value_frequency > highest_frequency:
        highest_frequency = current_value_frequency
        mode_array = DynamicArray()
        mode_array.append(current_value)
    elif current_value_frequency == highest_frequency:
        mode_array.append(current_value)

    return mode_array, highest_frequency

    # Run through the elements in the array once. O(N) complexity
    pass
# ------------------- BASIC TESTING -----------------------------------------

if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    def print_chunked_da(arr: DynamicArray):
        if len(str(arr)) <= 100:
            print(arr)
        else:
            print(f"DYN_ARR Size/Cap: {arr.length()}/{arr.get_capacity()}")
            print('[\n' + ',\n'.join(f'\t{chunk}' for chunk in arr) + '\n]')

    print("\n# chunk example 1")
    test_cases = [
        [10, 20, 30, 30, 5, 10, 1, 2, 3, 4],
        ['App', 'Async', 'Cloud', 'Data', 'Deploy',
         'C', 'Java', 'Python', 'Git', 'GitHub',
         'Class', 'Method', 'Heap']
    ]

    for case in test_cases:
        da = DynamicArray(case)
        chunked_da = chunk(da)
        print(da)
        print_chunked_da(chunked_da)

    print("\n# chunk example 2")
    test_cases = [[], [261], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]]

    for case in test_cases:
        da = DynamicArray(case)
        chunked_da = chunk(da)
        print(da)
        print_chunked_da(chunked_da)

    print("\n# find_mode example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")


