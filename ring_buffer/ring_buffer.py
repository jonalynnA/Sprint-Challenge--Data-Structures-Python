from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check to see if list is at capacity
        # if not append item to tail
        # if an item is already there, then append new item

        if self.storage.length < self.capacity:  # Check capacity -> if storage is not full

            self.storage.add_to_tail(item)  # append item to tail

            self.current = self.storage.head  # update current

        elif self.storage.length == self.capacity:  # Check capacity -> if storage is full

            oldest_node = self.storage.head  # remove the head to free space
            self.storage.remove_from_head()  # since it is the oldest
            self.storage.add_to_tail(item)  # add item to the tail (newest)

            if oldest_node == self.current:  # if we are at the head
                self.current = self.storage.tail  # set the current pos to the tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # loops through each node and appends the values
        c = self.current
        list_buffer_contents.append(c.value)

        if c.next:
            n = c.next

        else:
            n = self.storage.head

        while n != c:
            list_buffer_contents.append(n.value)

            if n.next:
                n = n.next

            else:
                n = self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass
