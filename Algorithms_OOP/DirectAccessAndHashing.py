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
"""

class DirectAccesArray:
    def __init__(self, u) -> None: self.Arr = [None] * u
    def find(self, value): return self.Arr[value]
    def insert(self, item): self.Arr[item.key] = item
    def delete(self, value): self.Arr[value] = None

    def find_next(self, value):
        for i in range(value, len(self.Arr)):
            if self.Arr[i] is not None:
                return self.Arr[i]
        