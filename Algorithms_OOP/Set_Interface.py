# Interface not a data structure - Since Data structure elaborate on how
# data is store and verbosely state how the operations affect what happens
# in the RAM and such details.


from OCW_Lectures.Interfaces_n_DStructures import Array_Seq

class SortedArraySet:
    def __init__(self) -> None: self.Arr = Array_Seq()
    def __len__(self) -> int: return len(self.Arr)
    def __iter__(self) -> list: yield from self.Arr
    
    def iter_order(self) -> list: yield from self

    def build(self, X):
        self.Arr.build(X)
        self._sort()

    def _sort(self):
        # TODO: find a way to implement a sort algorithm
        pass

    def _binary_search(self, search_item, lower, upper):
        if lower >= upper: return lower

        midpoint = (lower + upper) // 2
        checker = self.Arr.get_at(midpoint)

        if checker.key > search_item: return self._binary_search(search_item, lower, midpoint - 1)
        if checker.key < search_item: return self._binary_search(search_item, midpoint + 1, upper)

        return midpoint

    def find_min(self):
        # Check if empty if not return the first item since
        # it's already in sorted order
        if len(self) > 0: return self.Arr.get_at(0)
        else: return None

    def find_max(self):
        # Check if empty if not return the last item since 
        # it's already in sorted order
        if len(self) > 0: return self.Arr.get_at(len(self) - 1)
        else: return None

    def find(self, search_item):
        # Return None if the set is empty
        if len(self) == 0: return None
        # Retrieve the item at the position (or with the key in question)
        # of the item being searched for and compare the search term 
        # with the key of the retrieved value 
        index = self._binary_search(search_item, 0, len(self) - 1)
        retrieved = self.Arr.get_at(index)

        # Check for equality to get the item we're searching for 
        if retrieved.key == search_item: return retrieved
        else: return None

    def find_next(self, search_item):
        # Return None if the set is empty
        if len(self) == 0: return None
        # Retrieve the item at the position (or with the key in question)
        # of the item being searched for and compare the search term 
        # with the key of the retrieved value 
        index = self._binary_search(search_item, 0, len(self) - 1)
        retrieved = self.Arr.get_at(index)

        # Check for the greater value to get the previous item
        if retrieved.key > search_item: return retrieved
        if index + 1 < len(self): return self.Arr.get_at(index + 1)
        else: return None

    def find_prev(self, search_item):
        # Return None if the set is empty
        if len(self) == 0: return None
        # Retrieve the item at the position (or with the key in question)
        # of the item being searched for and compare the search term 
        # with the key of the retrieved value 
        index = self._binary_search(search_item, 0, len(self) - 1)
        retrieved = self.Arr.get_at(index)

        # Check for the lesser value to get the previous item
        if retrieved.key < search_item: return retrieved
        if index > 0: return self.Arr.get_at(index - 1)
        else: return None

    def insert(self, value):
        # If the set is empty we'll insert the value as the 
        # first item in the set
        if len(self.Arr) == 0:
            self.Arr.insert_first(value)
        else:
            # Otherwise if the key is already occupied override it with the new
            # value
            index = self._binary_search(value.key, 0, len(self.Arr) - 1)
            retrieved = self.Arr.get_at(index).key
            if retrieved == value.key:
                self.Arr.set_at(index, value)
                return False
            # if it's not occupied then append the item to the end of the set
            if retrieved > value.key: self.Arr.insert_at(index, value)
            else: self.Arr.insert_at(index + 1, value)

        return True

    def delete(self, value):
        index = self._binary_search(value, 0, len(self.Arr) - 1)
        assert self.Arr.get_at(index).key == value
        return self.Arr.delete_at(index)    
