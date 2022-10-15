from random import randint

def find_maximum_crossing_subarray(my_list, start_point, midpoint, end_point):
    left_sum = right_sum = -float('inf')
    sum_value = 0

    for i in range(start_point, (midpoint + 1)):
        sum_value += my_list[i]
        if sum_value > left_sum:
            left_sum = sum_value
            max_left_index = i
    sum_value = 0
    # if end_point - midpoint != 1:
    #     for j in range((midpoint + 1), end_point):
    #         sum_value += my_list[j]
    #         if sum_value > right_sum:
    #             right_sum = sum_value
    #             max_right_index = j
    # else:
    #     for j in range((midpoint), end_point):
    #         sum_value += my_list[j]
    #         if sum_value > right_sum:
    #             right_sum = sum_value
    #             max_right_index = j
    for j in range(end_point, midpoint, -1):
            sum_value += my_list[j]
            if sum_value > right_sum:
                right_sum = sum_value
                max_right_index = j

    return max_left_index, max_right_index, left_sum + right_sum


def find_maximum_subarray(my_list, low, high):
    midpoint = int((low + high)/2)
    if low == high:
        return low, high, my_list[high]
    else:
        left_low, left_high,left_sum = find_maximum_subarray(my_list, low, midpoint)
        right_low, right_high, right_sum = find_maximum_subarray(my_list, midpoint + 1, high)
        cross_low, cross_high, cross_sum = find_maximum_crossing_subarray(my_list, low, midpoint, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum

        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum

        else:
            return cross_low, cross_high, left_sum


def main():
    unordered_list = []
    for i in range(41):
        unordered_list.append(randint(-200,200))

    print(f"Trading Period:\n{ unordered_list }\n")
    max_left, max_right, current_sum = find_maximum_crossing_subarray(unordered_list, 0, int(len(unordered_list)/2), int(len(unordered_list)-1))
    print(f"Maximum Left Value Index:\n{ max_left }\n")
    print(f"Maximum Left Value:\n{ unordered_list[max_left] }\n")
    print(f"Maximum Right Value Index:\n{ max_right }\n")
    print(f"Maximum Right Value:\n{ unordered_list[max_right] }\n")
    print(f"Maximum Subarray Sum:\n{ current_sum }\n")

    print("==================================================")
    print("==================================================")

    final_low, final_high, final_sum = find_maximum_subarray(unordered_list, 0, int(len(unordered_list)-1))
    print(f"Maximum Final Low Index:\n{ final_low }\n")
    # print(f"Maximum Final Low:\n{ unordered_list[final_low] }\n")
    print(f"Maximum Final High Index:\n{ final_high }\n")
    # print(f"Maximum Final High:\n{ unordered_list[final_high] }\n")
    print(f"Tester Sum Value From index {final_low} to {final_high}:\n{ sum(unordered_list[final_low:final_high]) }\n")
    print(f"Tester Sum Value From index {0} to {final_high}:\n{ sum(unordered_list[0:final_high]) }\n")
    print(f"Maximum Final Sum:\n{ final_sum }\n")


main()
