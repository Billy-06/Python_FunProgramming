class TradingProfits:
    def __init__(self, iter_list):
        self.my_list = [0]
        for i in range(len(iter_list)):
            if i + 1 < len(iter_list):
                self.my_list.append(iter_list[i+1] - iter_list[i])
                
        self.left_sum = -float("inf")
        self.right_sum = -float("inf")
        self.cross_sum = -float("inf")
        self._low = 0
        # self._mid = int(self.my_list / 2)
        self._high = int(len(self.my_list) - 1)
        self.max_left_index = 0
        self.max_right_index = 0
        self.low_val = 0
        self.high_val = 0
        self.sum_val = 0

    def __str__(self):
        return f"Implementation of the Maximum Sub-Array Problem - presumed to be on a Trading Platform"

    def maximum_crossing_subarray(self, my_list, low, mid, high):
        sum = 0
        for i in range(mid, low - 1, -1):
            # Add values from the middle down to the left.
            # This allows us to gradually disposed the further left values
            # that don't give us the desired output.
            sum += my_list[i]
            # Any time the sum exceeds the maximum stored value of the sum
            # update it and take note of that index upon which the sum hit
            # a new max.
            if sum > self.left_sum:
                self.left_sum = sum
                # Store the index upon whereof the sum hit max
                self.max_left_index = i
        
        sum = 0
        for j in range(mid + 1, high + 1):
            # Add values from the middle towards the far right.
            sum += my_list[j]
            # Any time the sum exceeds the maximum stored value of the sum
            # update it and take note of that index upon which the sum hit
            # a new max.
            if sum > self.right_sum:
                self.right_sum = sum
                # Store the index upon whereof the sum hit max
                self.max_right_index = j
        
        # add the left & right sums produced if to find the sum if
        # the arrays crossed the mid point.
        self.cross_sum = self.left_sum + self.right_sum

        return self.max_left_index, self.max_right_index, self.cross_sum


    def maximum_subarray(self, my_list, start_point, end_point):

        if start_point == end_point:
            return start_point, end_point, my_list[end_point]
        else:
            midpoint = int((start_point + end_point)/2)

            self.left_low, self.left_high, self.left_sum = self.maximum_subarray(
                my_list, start_point, midpoint
            )
            self.right_low, self.right_high, self.right_sum = self.maximum_subarray(
                my_list, midpoint + 1, end_point
            )
            self.cross_low, self.cross_high, self.cross_sum = self.maximum_crossing_subarray(
                my_list, start_point, midpoint, end_point
            )
        
            if self.left_sum >= self.right_sum and self.left_sum >= self.cross_sum:
                return self.left_low, self.left_high, self.left_sum

            elif self.right_sum >= self.left_sum and self.right_sum >= self.cross_sum:
                return self.right_low, self.right_high, self.right_sum

            else:
                return self.cross_low, self.cross_high, self.cross_sum
    
    def find_subarray(self):
        self.low_val, self.high_val, self.sum_val = self.maximum_subarray(self.my_list, self._low, self._high)

        return f"Low Index:\n{self.low_val}\nHigh Index:\n{self.high_val}\nMain Array\n{self.my_list}\nSubarray\n{self.my_list[self.low_val:self.high_val]}\nSum Value:\n{self.sum_val}"


# This object is a matrix multiplier, which takes two nxn matrices as
# parameters and returns their dot product
class SquareMatrixDot:
    def __init__(self, matrix_a, matrix_b):
        pass

def find_max_crossing_subarray(my_list, low, mid, high):
    left_sum = float("inf")
    right_sum = float("inf")
    max_left = 0
    cross_sum = 0
    max_right = 0
    
    sum_value = 0
    for item in range(mid, low - 1, -1):
        sum_value += my_list[item]
        if sum_value > left_sum:
            left_sum = sum_value
            max_left = item
    
    sum_value = 0
    for iter in range(mid + 1, high + 1):
        sum_value += my_list[iter]
        if sum_value > right_sum:
            right_sum = sum_value
            max_right = iter
    
    cross_sum = left_sum + right_sum

    return max_left,  max_right, cross_sum

def find_max_subarray(my_list, low, high):
    # Constantly check whether we've found the base case
    if low == high:
        return low, high, my_list[high] # base case where we only have one element.
    else:
        # since we've not yet found a base case we'll keep iterating
        mid = int((low + high)/2)

        left_low, left_high, left_sum = find_max_subarray(my_list, low, mid)
        right_low, right_high, right_sum = find_max_subarray(my_list, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(my_list, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

def find_subarray(my_list):
        low_val, high_val, sum_val = find_max_subarray(my_list, 0, len(my_list) -1)

        return f"Low Index:\n{low_val}\nHigh Index:\n{high_val}\nMain Array\n{my_list}\nSubarray\n{my_list[low_val:high_val]}\nSum Value:\n{sum_val}"

def main():
    from random import randint
    random_list = []

    extracted = [0, 13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

    test_array = [100,113,110,85,105,102,86,63,81,101,94,106,101,79,94,90,97]

    for _ in range(40):
        random_list.append(randint(80, 350))

    print(find_subarray(extracted))
    # trader = TradingProfits(random_list)
    # tester = TradingProfits(test_array)
    # print(f"List of Trade Stocks:\n{test_array}")
    # print(tester.find_subarray())

    


main()