# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:


from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        Adds a new element to the end of the queue
        """
        # Create a new node for the new value
        new_node = SLNode(value)

        # If the queue is empty, set head and tail to the new node
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            # Have the tail point to the new node, then set the tail to be the new node
            self._tail.next = new_node
            self._tail = new_node

        pass

    def dequeue(self) -> object:
        """
        Removes the value at the beginning of the que and returns it
        """
        # Handle cases where the que is empty
        if self.is_empty():
            raise QueueException('Queue is empty')

        # Get the value from the head_node and move head the next node
        front_value = self._head.value
        self._head = self._head.next

        # If head becomes none set the tail to be none as well
        if self._head is None:
            self._tail = None

        return front_value

        pass

    def front(self) -> object:
        """
        Returns the front value of the queue without removing it.
        """

        # Handle cases where the que is empty
        if self.is_empty():
            raise QueueException('Queue is empty')

        return self._head.value
        pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
