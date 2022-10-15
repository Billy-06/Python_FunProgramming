from random import randint

def merge(my_list : list, start_point : int, midpoint: int, end_point: int) -> list:
    first_batch = midpoint - (start_point + 1)
    second_batch = end_point - midpoint

    # Divide - Split the main Array into halves that can be subdued
    sub_array_one = []
    sub_array_two = []
    for i in range(first_batch):
        sub_array_one.append(my_list[start_point + i])

    for j in range(1, second_batch):
        sub_array_two.append(my_list[end_point + j])

    #sub_array_one[first_batch + 1] = 456789
    #sub_array_two[secon_batch + 1] = 456789
    i = j = 0

    # Combine the sorted subarrays into a fully sorted one
    for k in range(start_point,end_point):
        if sub_array_one[i] <= sub_array_two[j]:
            my_list[k] = sub_array_one[i]
            i += 1
        else:
            my_list[k] = sub_array_two[j]
            j += 1

    return my_list


def merge_sort(my_list: list, start_point: int, end_point: int):
    if start_point < end_point:
        midpoint = int((start_point + end_point)/2)
        # Perform recursion to keep disecting the array till
        # we reach the base case of the recursion namely, start
        merge_sort(my_list, start_point, midpoint)
        merge_sort(my_list, midpoint + 1, end_point)
        my_list = merge(my_list, start_point, midpoint, end_point)

    return my_list

def main():
    random_list = []
    for i in range(50):
        random_list.append(randint(0, 456))

    print(f"Unordered List:\n{ random_list }")
    sorted_list = merge_sort(random_list,0, len(random_list) - 1)
    print(f"Ordered List:\n{ sorted_list }")

    
main()
