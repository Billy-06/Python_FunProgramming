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
    
    def delete_max(self):
        for i in range(len(self.Arr) - 1, -1, -1):
            deleted = self.Arr[i]
            if deleted is not None:
                self.Arr[i] = None
                return deleted

        
class HashTableSet:
    def __init__(self, ratio = 200) -> None:
        from random import randint
        self.chain_set = SetFromSequence(LinkedListSeq)
        self.Arr = []
        self.size = 0
        self.ratio = ratio
        # Number of possible inputs picked from a family of hash 
        # hash functions
        # p = possibles 
        self.possibles = 2**31 - 1
        # Example of a hash family
        # H(m,p) = { hab(k) = (((ak + b) mod p) mod m) a,b ε {0,....,p-1} and a != 0 }
        self.a = randint(1, self.possibles - 1)
        self._compute_bounds()
        self._resize(0)

    # The length operation takes O(1) time
    def __len__(self): return self.size

    def __iter__(self):
        for X in self.Arr:
            yield from X

    def build(self, Arr):
        for item in Arr: self.insert(item)

    def _hash(self, keys, hash_size):
        return ((self.a * keys) % self.possibles) % hash_size

    def _compute_bounds(self):
        self.upper = len(self.Arr)
        self.lower = len(self.Arr) * (100 * 100)//(self.ratio * self.ratio)

    def _resize(self, overall_size):
        if (self.lower >= overall_size) or (overall_size >= self.upper):
            f = self.ratio // 100
            if self.ratio % 100: 
                f += 1
            m = max(overall_size, 1) * f
            Arr = [self.chain_set() for _ in range(m)]
            for x in self:
                h = self._hash(x.key, m)
                Arr[h].insert(x)
            self.Arr = Arr
            self._compute_bounds()