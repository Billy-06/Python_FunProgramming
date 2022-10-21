"""
            Operation, Worst Case O(.)
--------------------|-----------|-----------|---------------|--------------|-------------|
                    |Container  |Static     |           Dynamic                          |
--------------------|-----------|-----------|---------------|--------------|-------------|
                    |build(X)   | find(k    |insert(x)      |find_min()    |find_prev(k) |
Data Structure      |           |           |delete(k)      |find_max()    |find_next(k) |
--------------------|-----------|-----------|---------------|--------------|-------------|
Static Array        |    n      |    n      |       n       |       n      |      n      |
Sorted Array        |    nlog n |    log n  |       n       |       1      |      log n  |
Direct Access Array |    u      |    1      |       1       |       u      |      u      |    
Hash Table          |    n(e)   |    1(e)   |       1(a)(e) |       n      |      n      |    
--------------------|-----------|-----------|---------------|--------------|-------------|

Legend:
    1(a): Amortized time
    1(e): Expected time

"""

from Algorithms_OOP.Interfaces_n_DStructures import LinkedListSeq, SetFromSequence


class DirectAccessArray:
    def __init__(self, u) -> None: self.Arr = [None] * u
    def find(self, value): return self.Arr[value]
    def insert(self, item): self.Arr[item.key] = item
    def delete(self, value): self.Arr[value] = None

    def find_next(self, value):
        for i in range(value, len(self.Arr)):
            if self.Arr[i] is not None:
                return self.Arr[i]

    def find_max(self):
        for i in range(len(self.Arr) - 1, -1, -1):
            if self.Arr[i] is not None:
                return self.Arr[i]
    
    def find_max(self):
        for i in range(len(self.Arr) - 1, -1, -1):
            deleted = self.Arr[i]
            if deleted is not None:
                self.Arr[i] = None
                return deleted

        
class HashTableSet:
    def __init__(self, ratio = 200) -> None:
        self.chain_set = SetFromSequence(LinkedListSeq)
        self.Arr = []
        self.size = 0
        self.ratio = ratio
        self.p = 2**31 - 1