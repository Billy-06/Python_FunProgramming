"""
            Operation, Worst Case O(.)
--------------------|-----------|-----------|---------------|--------------|-------------|
                    |Container  |Static     |           Dynamic                          |
--------------------|-----------|-----------|---------------|--------------|-------------|
                    |build(X)   |get_at()   |insert_first(x)|insert_last(x)|insert_at(x) |
Data Structure      |           |set_at()   |delete_first() |delete_last() |delete_at(i) |
--------------------|-----------|-----------|---------------|--------------|-------------|
Static Array        |    n      |    1      |       n       |       n      |      n      |
Linked List         |    n      |    n      |       1       |       n      |      n      |    
Dynamic Array       |    n      |    1      |       n       |       1      |      n      |    
--------------------|-----------|-----------|---------------|--------------|-------------|
"""

class Array_Seq:
    def __init__(self) -> None:
        self.Arr = []
        self.size = 0
        
    def __len__(self) -> int: return self.size
    def __iter__(self) -> list: yield from self.Arr

    def build(self, X):
        # We're making the assumption that this implements a static Array
        self.Arr = [item for item in X]
        self.size = len(self.Arr)


    def get_at(self, index) -> int: return self.Arr[index]
    def set_at(self, index, value) -> None: self.Arr[index] = value

    def _copy_forward(self, index, pos, Arr, arr_index) -> None:
        # This operation will take O(n) time to execute 
        for k in range(pos):
            Arr[arr_index + k] = self.Arr[index + k]

    def _copy_backward(self, index, pos, Arr, arr_index) -> None:
        # This operation will take O(n) time to execute 
        for k in range(pos - 1, -1, -1):
            Arr[arr_index + k] = self.Arr[index + k]

    def insert_at(self, index, value) -> None:
        # This will take O(n) time to implement since it involves
        # reallocating space in memory for the new size of the array
        
        # Obtian the size of the current array and instantiate a new
        # array of size n+1 
        n = len(self) 
        Arr = [None] * (n + 1)
        # Insert value at position index in the new Array and move
        # the rest of the items forward 
        self._copy_forward(0, index, Arr, 0)
        Arr[index] = value
        # Set the rest of the items in the list to start copying from
        # index + 1 
        self._copy_forward(index, n - index, Arr, index + 1)
        self.build(Arr)

    def delete_at(self, index) -> int:
        # This operation will take O(n) time since we'll be required
        # to reassign the memory space to the array
        # 
        # Obtain the size of the origininal array and construct a new
        # empty array of size n-1
        n = len(self)
        Arr = [None] * (n-1)

        # Copy all the items in the original array into the new array
        # from position 0 until position index 
        self._copy_forward(0, index, Arr, 0)
        deleted = self.Arr[index]
        
        # Replace the old value destructively by overiting the position
        # index with the value previously next to it. Copy the rest
        # of the items from position index to n-1 
        self._copy_forward(index + 1, n - index - 1, Arr, index)
        self.build(Arr)
        return deleted

    def insert_first(self, value) -> None: self.insert_at(0, value)
    def delete_first(self) -> int: return self.delete_at(0)
    def insert_last(self, value) -> None: self.insert_at(len(self), value)
    def delete_last(self) -> int: return self.delete_at(len(self) - 1)



# Implementation of Linked List Sequence

class LinkedListNode:
    def __init__(self, value) -> None:
        # This operation will take O(1)
        self.item = value
        self.next = None
        
    def later_node(self, index):
        # This is a recursive function meant to walk over to position
        # index by continually calling the function in a comparison model
        # manner till it finds the item at position index 
        if index == 0: return self
        assert self.next
        return self.next.later_node(index - 1)

class LinkedListSeq:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def __len__(self): return self.size
    def __iter__(self):
        # It takes O(n) time to iterate through the linked list 
        node = self.head
        while node:
            yield node.item
            node = node.next

    def build(self, X):
        # Building will take O(n) time since it'll implement every single
        # item in the linked list individually  
        for a in reversed(X):
            self.insert_first(a)

    def get_at(self, index):
        # This operation takes linear time since the algorithm will need
        # to walk all the way to position index
        node = self.head.later_node(index)
        return node.item

    def set_at(self, index, value):
        # Same case here the algorithm will need to walk to position index
        # in order to set the value 
        node = self.head.later_node(index)
        node.item = value

    def insert_first(self, value):
        # This op takes O(1) expectedly it only needs to check the first
        # item in the Linked List
        new_node = LinkedListNode(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete_first(self):
        # This operationexpectedly takes O(1) since it only need to check
        # the first item in the linked list 
        deleted = self.head
        self.head = self.head.next
        self.size -= 1
        return deleted.item

    def insert_at(self, index, value):
        if index == 0:
            self.insert_first(value)
            return

        new_node = LinkedListNode(value)
        
        # Use the recursive function later_node() to walk over to
        # the desired position and retrieve the node of interest then
        # attach the new node after the node behind position index (index - 1) 
        node  = self.head.later_node(index - 1)
        new_node.next = node.next
        node.next = new_node
        self.size += 1

    def delete_at(self, index):
        if index == 0:
            return self.delete_first()

        # Walk over to position (index - 1) and detach the node at index-1
        # from the node at index by setting its next item to node.next.next
        # the return the deleted value  
        node = self.head.later_node(index - 1)
        deleted = node.next.item
        node.next = node.next.next
        self.size -= 1
        return deleted

    # Insert Last & Delete Last operations will take O(n) since
    # we'll have to walk to the very last node 
    def insert_last(self, value): self.insert_at(len(self), value)
    def delete_last(self): return self.delete_at(len(self) - 1)

class DynamicArraySeq(Array_Seq):
    # Dynamic Arrays create a little more extra space O(n) time
    # to contain items m where m is roughly ~ n/2. This
    # allows for appending and deletions that take much less
    # time because of not having to reallocate memory all over again.
    # After a few operations however the array would nee to assign more
    # memory to accomodate the growth of Array m 
    def __init__(self, recursions=2) -> None:
        super().__init__()
        self.size = 0
        self.recursions = recursions
        self._compute_bounds()
        self.resize(0)

    def __len__(self) -> int: return self.size
    def __iter__(self) -> list:
        # Iterating through the entire array will take O(n) time
        for i in range(len(self)) : yield from self.Arr[i]

    def build(self, X):
        # Builind will take O(n)
        for a in X: self.insert_last(a)

    def _compute_bounds(self) -> None:
        self.upper = len(self.Arr)
        self.lower = len(self.Arr) // self.recursions

    def _resize(self, n) -> None:
        if (self.lower < n < self.upper): return
        # Resize to the number od recursions passed
        # check if the number is greater than 1 
        m = max(n, 1) * self.recursions
        # Create an array with the size m
        # and add items to it using copy forward 
        Arr  = [None] * m
        self._copy_forward(0, self.size, Arr, 0)
        self.Arr = Arr
        # Calculate the new upper and lower bounds of the array 
        self._compute_bounds()

    def insert_last(self, value) -> None:
        self._resize(self.size + 1)
        self.Arr[self.size + 1] = value
        self.size += 1

    def delete_last(self) -> None:
        self.Arr[self.size - 1] = None
        self.size -= 1
        self._resize(self.size)

    def insert_at(self, index, value) -> None:
        self.insert_last(None)
        self._copy_backward(index, self.size - (index + 1), self.Arr, index + 1)
        self.Arr[index] = value

    def delete_at(self, index) -> int:
        deleted = self.Arr
        self._copy_forward(index + 1, self.size - (index + 1), self.Arr, index)
        self.delete_last()
        return deleted

    def insert_first(self, value) -> None: self.insert_at(0, value)
    def delete_first(self) -> int: return self.delete_at(0)


"""
    Implementing a Set from a Sequence
"""

def SetFromSequence(seq):
    class SetFromSeq:
        def __init__(self) -> None: self.Set = seq()
        # Getting the length takes O(n) time
        def __len__(self) -> int: return len(self.Set)
        def __iter__(self) -> list: yield from self.Set

        def build(self, Arr):
            self.Set.build(Arr)

        def insert(self, value) -> int:
            for i in range(len(self.Set)):
                if self.Set.get_at(i).key == value.key:
                    self.Set.set_at(i, value)
                    return
            self.Set.insert_last(value)
            
        def delete(self, k):
            for i in range(len(self.Set)):
                if self.Set.get_at(i).key == k:
                    return self.Set.delete_at(i)

        def find(self, k):
            for x in self:
                if x.key == k: return x
            return None

        # In the operations that follow, there'll be some similarities
        # as we implement the find_min(), find_max(), find_next(), find_prev() functions
        # Create a variable to start the operation
        # we'll check if this variable is set to the 
        # initially assigned value to decide whether to start or stop the operation
        # 
        # Assumption: We're assuming the keys are integer keys for this implementation
        #  

        def find_min(self):
            output = None
            for x in self:
                if (output is None) or (x.key < output.key):
                    output = x

            return output

        def find_max(self):
            output = None
            for x in self:
                if (output is None) or (x.key > output.key):
                    output = x

            return output

        def find_next(self, value):
            output = None
            for x in self:
                if x.key > value:
                    if (output is None) or (x.key < output.key):
                        output = x

            return output

        def find_prev(self, value):
            output = None
            for x in self:
                if x.key < value:
                    if (output is None) or (x.key > output.key):
                        output = x

            return output

        # Iterating through the Set in an ordered fashion
        def iter_ordered(self):
            value = self.find_min()
            while value:
                yield value
                value = self.find_next(value.key)
    
    return SetFromSeq
