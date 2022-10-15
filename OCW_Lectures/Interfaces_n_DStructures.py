from dataclasses import dataclass

class StaticSeq:
    def __init__(self, len=50, minimum=-2000, maximum=2000):
        self.my_list = []
        self.lower = minimum
        self.upper = maximum

    def build(self, iterable: int):
        self.length = iterable
        from random import randint
        for i in range(self.length):
            self.my_list.append(randint(self.lower, self.upper))

        return self.my_list

    def length(self):
        self.size = 0
        for i in range(self.my_list):
            self.size += 1
        return self.size

    def iter_seq(self):
        pass

    def get_at(self, index):
        pass

    def set_at(self, index, value):
        pass


class DynamicSeq:
    def __init__(self, len=50, minimum=-2000, maximum=2000):
        self.my_list = []
        self.lower = minimum
        self.upper = maximum

    def build(self, iterable: int):
        self.length = iterable
        from random import randint
        for i in range(self.length):
            self.my_list.append(randint(self.lower, self.upper))

        return self.my_list

    def length(self):
        self.size = 0
        for i in range(self.my_list):
            self.size += 1
        return self.size

    def iter_seq(self):
        pass

    def get_at(self, index):
        pass

    def set_at(self, index, value):
        pass

    def insert_at(self, index, value):
        pass

    def delete_at(self, index):
        pass


class SingleNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next



class LinkedList:
    def __init__(self, head, tail) -> None:
        pass

    def display(self) -> None:
        pass
    