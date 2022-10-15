import heapq
from random import randint
from typing import final

my_list = []
# my_heap = heapq
# for _ in range(20):
#     heapq.heappush(my_list, randint(-400, 400))

# print(my_list)
# print(type(my_list))

class HeapNode:
    def __init__(self, value):
        self.value = value
        self.left_val = 2*value
        self.right_val = (2*value) + 1

    def check_binary(self):
        quotient = self.value
        binary_list = []

        self.final_str = ""

        while quotient >= 1:
            if quotient % 2 == 0:
                binary_list.append("0")
            else:
                binary_list.append("1")

            quotient //= 2

        for item in binary_list:
            # this way the string will be reversed
            self.final_str = item + self.final_str

        # self.final_str = "0x" + self.final_str
        return self.final_str

    

def parent(item: int) -> int:
    return item/2

def leftnode(item: int) -> int:
    return 2*item

def rightnode(item: int) -> int:
    return 2*item + 1

def check_binary(my_value):
    quotient = my_value
    binary_list = []
    final_str = ""

    while quotient >= 1:
        if quotient % 2 == 0:
            binary_list.append("0")
        else:
            binary_list.append("1")

        quotient //= 2

    for item in binary_list:
        # this way the string will be reversed
        final_str = item + final_str
    # final_str = "0x" + final_str
    return final_str

print(f"Number 6 in binary is: {check_binary(6)}")
print(f"Number 29 in binary is: {check_binary(29)}")
print(f"Number 30 in binary is: {check_binary(30)}")
