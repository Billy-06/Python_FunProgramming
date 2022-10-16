import heapq
from random import randint

my_list = []

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

        return self.final_str

# Selection Sort
def selection_sort(my_list) -> list:
    for i in range(len(my_list) - 1, 0, -1):
        m = i
        for j in range(i):
            if my_list[m] < my_list[j]:
                m = j
        # Swap the values
        my_list[m], my_list[i] = my_list[i], my_list[m]

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
