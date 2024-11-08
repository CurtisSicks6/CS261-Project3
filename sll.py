# Name: Curtis Sicks
# OSU Email: sicksc@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Linked List and ADT Implementation
# Due Date: 11/04/24
# Description: Implementation of Linked List data structure and ADTs (Stack and Queue).


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        Adds a new node after the front sentinel.
        """

        # Create added node containing given value
        added_node = SLNode(value)

        # Have the added node's next argument point to next value after the front sentinel
        added_node.next = self._head.next

        # Have the front sentinel next argument point to the added node
        self._head.next = added_node

        pass

    def insert_back(self, value: object) -> None:
        """
        Add a new node to the end of the list.
        """

        # Create the new node and start at the sentinel node
        added_node = SLNode(value)
        current_node = self._head

        # Pass through the linked list entirely. Only when the last node points to None do we insert
        # the added node.

        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = added_node

        # We pass through all elements of the list, thus making the operation of O(N) complexity
        pass

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts the given value at the specified position of the list. Raise an SLLException
        if the index is out of bounds.
        """
        # Handle Out of Bounds index
        if index < 0 or index > self.length():
            raise SLLException("Index is out of Bounds")

        # Create new node, start at sentinel node, initialize index
        added_node = SLNode(value)
        current_node = self._head
        current_index = 0

        # Move through the list until we reach the specified index
        while current_index < index:
            current_node = current_node.next
            current_index += 1

        # Have the new node point to node the current node is pointing to,
        # then have current node point to the added node
        added_node.next = current_node.next
        current_node.next = added_node

        # Worst case scenario, we have to pass through the full list to reach the specified index so O(N) complexity.

        pass

    def remove_at_index(self, index: int) -> None:
        """
        Removes the node that is present at the specified index. Raise an SLLException
        if the index is out of bounds.
        """
        # Handle Out of Bounds index
        if index < 0 or index >= self.length():
            raise SLLException("Index is out of Bounds")

        # Start at sentinel node, initialize index
        current_node = self._head
        current_index = 0

        # Move through the list until we reach the specified index
        while current_index < index:
            current_node = current_node.next
            current_index += 1

        # The pointer for the current node should now skip the node we want to remove and point to the
        # node ahead of it
        current_node.next = current_node.next.next

        # Worst case scenario, we have to pass through the full list to reach the specified index so O(N) complexity.

        pass

    def remove(self, value: object) -> bool:
        """
        Removes the first node that matches the provided value.
        If a node is removed, return true. Return False if not.
        """

        # Start at sentinel node
        current_node = self._head

        # Work through the list looking for the passed value.
        while current_node.next is not None:
            if current_node.next.value == value:
                # The pointer for the current node should now skip the node we want to remove and point to the
                # node ahead of it.
                current_node.next = current_node.next.next
                return True
            current_node = current_node.next

        # If no node value matches, return False
        return False

        # Worst case scenario, we have to pass through the full list to reach to find a matching node value, so O(N).
        pass

    def count(self, value: object) -> int:
        """
        Counts the number of elements in the list that match the provided value. Returns the count.
        """

        # Initialize count and start front sentinel
        count = 0
        current_node = self._head

        # Iterate through the list, counting the number of times we pass an equal value
        while current_node.next is not None:
            if current_node.value == value:
                count += 1
            current_node = current_node.next

        # Run one last check for the final node in the list.
        if current_node.next is None:
            if current_node.value == value:
                count += 1

        return count

        # We have to pass through the full list to ensure our count is correct, so O(N).
        pass

    def find(self, value: object) -> bool:
        """
        Looks to see if value exist in list. Returns true if it does and false if it doesn't
        """
        # Begin at the first node (not the front sentinel)
        current_node = self._head.next

        # Search through the list for a node with a matching element
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next

        return False

        # At worst, we have to pass through the full list to ensure the value is or isn't present, so O(N).

        pass

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        This method returns a new LinkedList that contains the requested number of nodes from the
        original list, starting with the node located at the requested start index.
        """

        # Handle invalid cases
        if start_index < 0 or start_index >= self.length() or size < 0:
            raise SLLException("Start index and/or size is invalid")

        if start_index + size > self.length():
            raise SLLException("Not enough nodes to create requested slice")

        # Create a new list for spliced elements
        new_list = LinkedList()

        # Move current_node to the start index
        current_node = self._head.next
        for x in range(start_index):
            current_node = current_node.next

        # Create spliced LinkedList
        for x in range(size):
            new_list.insert_back(current_node.value)
            current_node = current_node.next

        return new_list

        # At worst, we have to pass through the full list to ensure the value is or isn't present, so O(N).

        pass


if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
