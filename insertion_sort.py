# Insertion Sort runs in O(n^2) time. This means it grows quadratically depending upon the
# size of the data provided.
# To implement the insertion sort, write a functions that takes a parameter - which would 
# the candidate list.
# ------------------------------------------------------------------------------- 
# LOOP INVARIANT: The loop invariant is the state of the loop at any given time.
# ------------------------------------------------------------------------------- 
# Assertain the the implementation satisfies the three rules of algorithms
# Rule 1 - Initialization:>> The state (Loop Invariant) that triggers initialization
#                           At the very beginning j == 0 is true however single value is 
#                           considered ordered. Note that in the implmentation I start 
#                           with i = 1 and keep checking it against the preceeding
#                           values (Reason: I don't have to add an extra condition
#                           checker to prevent j being -1 (since j = i - 1) as this
#                           would reference the last item in the array.)
# Rule 2 - Maintenance  :>> The swaping (interchanging items in the list - which is a 
#                           3 step process) only happens when j >= 0 and the item at index j
#                           is greater or less than the current value (depending on whether it's
#                           being ordered in ascending or descending order)
# Rule 3:>> Termination :>> The loop only terminates when either one of the conditions j >= 0
#                           and the item at index j is less than or greater than the current values
#                           (depending on the sorting order), is not fulfilled.

"""
    > A python class on Insertion Sort Algorithm - Object representing the 
        insertion sort algorithm.
"""
class Insertion:
    # Initialisation of the class
    def __init__(self, my_list):
        self.my_list  = my_list

    # Create the string representation of the class
    def __str__(self):
        return f"Insertion Sort Algorithm"

    def _write_to_file(self, data, order):
        try:
            with open(f"{order}.txt", "w+") as filename:
                filename.write(data)
        except:
            print(f"Couldn't write to {order}.txt")

    # Create and ascending order of the algorithm
    def ascending(self):
        # Iterate through every single element of the list checking 
        # if it's greater than its preceeding item.
        # Start from 1 that way the loop invariant can be maintained
        # since j = i - 1
        for i in range(1, len(self.my_list)):
            current_value = self.my_list[i]
            j = i - 1
            while j >= 0 and self.my_list[j] > current_value:
                # The loop invariant requires that j be both greater than 0
                # and the item at index j be greater than the current value.
                # As long as this is true we'll swap the values around till 
                # the conditions aren't both true (it's likely that j will always
                # be greater than 0 but not necessarily as likely that the item
                # at index j be grater than the current value) then we'll place 
                # the current value at the most recent j position
                self.my_list[j + 1] = self.my_list[j]
                j -= 1
            
            # Now assign the position j + 1 to the current value
            self.my_list[j + 1] = current_value
        
        # self._write_to_file("ascending", self.my_list)
        return (f"\nOrdered as Ascending List:\n===============================\n{self.my_list}")

    def descending(self):
        # Iterate through every single element of the list checking 
        # if it's greater than its preceeding item.
        # Start from 1 that way the loop invariant can be maintained
        # since j = i - 1
        for i in range(1, len(self.my_list)):
            current_value = self.my_list[i]
            j = i - 1
            while j >= 0 and self.my_list[j] < current_value:
                # The loop invariant requires that j be both greater than 0
                # and the item at index j be less than the current value.
                # As long as this is true we'll swap the values around till 
                # the conditions aren't both true (it's likely that j will always
                # be greater than 0 but not necessarily as likely that the item
                # at index j be grater than the current value) then we'll place 
                # the current value at the most recent j position
                
                self.my_list[j + 1] = self.my_list[j]
                j -= 1
            
            # Now assign the position j + 1 to the current value
            self.my_list[j + 1] = current_value
        
        # self._write_to_file("descending", self.my_list)
        return (f"\nOrdered as Descending List:\n===============================\n{self.my_list}")
        

## Divide & Conquer .. then Combine :)
# Merge Sort's best case scenario would take O(n) (This is where 
# the (end_point - start_point + 1) == len(my_list)) time to sort an array. 
# Its worst case takes O(nlogn) time to sort an array. 
# Divide        :>> Divide the problem into managable sizes
# Conqure       :>> Sort the small sizes within themselves
# Combine       :>> Combine the sorted sections into one whole sorted list

class MergeSort:
    def __init__(self, my_list):
        self.my_list = my_list
        # Divide the array into subarrays left_side & right_side of sizes n/2
        self._left_side = []
        self._right_side = []

    def merge_sort(self, my_list, start_point, end_point):
        
        if start_point < end_point:
            midpoint = int((start_point + end_point)/2)
            self.merge_sort(my_list, start_point, midpoint)
            self.merge_sort(my_list, midpoint + 1, end_point)
            self._merge(my_list, start_point, midpoint, end_point)
        
        return (f"Ascending Ordered List:\n{my_list}")


    def _merge(self, my_list, start_point, midpoint, end_point):
        # The new sub arrays with each contain first_batch items and second_batch items
        # Adding a +1 to the first batch makes sure we include the midpoint

        first_batch = (midpoint - start_point) + 1
        second_batch = (end_point - midpoint)

        print("\nCreating the leftside subarray\n")
        for i in range(first_batch):
            # left_index = start_point + i
            self._left_side.append(my_list[start_point + i])
        
        print(self._left_side)

        print("\nCreating the rightside subarray\n")
        for j in range(1,second_batch + 1):
            self._right_side.append(my_list[midpoint + j])

        print(self._right_side)

        # LOOP INVARIANT
        # Initialization:>> Having two unordered subarrays the left_side[0] and right_side[0]
        #                   either equal or unequal are compared then the least of the two is 
        #                   assigned to the final combined array (which starts from [k=start_point]
        #                   to the end of the array)
        # Maintenance   :>> Increamenting i and j is done independently. Keeping in mind the left_side
        #                   and right_side array are already ordered (preventing an instance of error
        #                   in the final combination) if a value sitting at left_side[i] is greater 
        #                   than a value at right_side[j] then index i is not incremented till all values
        #                   lesser than left_side[i] from right_side are ordered into the final combination
        # Termination   :>> At termination the following statementes are true: 
        #                   (a) k = end_pont + 1 
        #                   (b) my_list[start_point:midpoint - 1] <= my_list[midpoint] <= my_list[(midpoint + 1):end_point]
        #                   point b satisfies the law of trichotomy in ordering.
        i = 0
        j = 0
        for k in range(start_point, len(my_list) - 1):
            if self._left_side[i] <= self._right_side[j]:
                my_list[k] = self._left_side[i]
                if i + 1 < first_batch:
                    i += 1
            else:
                my_list[k] = self._right_side[j]
                if j + 1  < second_batch:
                    j += 1
        
        # return (f"Ascending Ordered List:\n{my_list}")

# Bubble Sort Algorithm
# 
class BubbleSort:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return f"Bubble Sort Algorithm"

    def ascending(self):
        for i in range(len(self.my_list)):
            for j in range(len(self.my_list) - 1, i + 1, -1):
                if self.my_list[j - 1] > self.my_list[j]:
                    container = self.my_list[j - 1]
                    self.my_list[j - 1] = self.my_list[j]
                    self.my_list = container
        
        return f"Ordered as Ascending:\n{self.my_list}"

    def descending(self):
        for i in range(len(self.my_list)):
            for j in range(len(self.my_list) - 1, i + 1, -1):
                if self.my_list[j - 1] < self.my_list[j]:
                    container = self.my_list[j - 1]
                    self.my_list[j - 1] = self.my_list[j]
                    self.my_list = container
        
        return f"Ordered as Descending:\n{self.my_list}"


# On trading platforms, maximizing profit is based upon knowing when to buy the stock (when
# they're low in price) and when to sell (when the price is high). If the future prices are
# known we can use an algorithm that checks the maximum days whereof the daily changes/differences
# have the maximum sum of all set of days within the trading period, as this 
# would mean buying at the start of this span of days and selling at the end would make 
# the trader the most profit possible. We therefore need to be able to return the subarray 
# (representative of the best set of days during which one should trade, buying at the beginning 
# and selling at the end of the set of days) whose daily differences sum up to give the largest
# value.
class TradingProfits:
    def __init__(self, my_list):
        self.my_list = my_list
        self._left_sum = -float("inf")
        self._right_sum = -float("inf")
        self._low = None
        self._mid = None
        self._high = None
        self.max_left_sum = 0
        self.max_right_sum = 0

    def __str__(self):
        return f"Implementation of the Maximum Sub-Array Problem - presumed to be on a Trading Platform"

    def maximum_crossing_subarray(self, my_list, low, mid, high):
        sum = 0
        pass

    def maximum_subarray(self):
        pass

class MaxSubArrayOne:
    def __init__(self, my_list):
        self.my_list = my_list
        self.maximum_sum = 0
        self.differences_list = [0]
        self.sum_values = 0
        self.pairs_indices = []

    def _add_items(self, my_iterable):
        total_added = 0
        for iter in range(len(my_iterable)):
            total_added += my_iterable[iter]
        return total_added

    def max_subarray(self):
        # Find the differences
        for i in range(len(self.my_list)):
            if i + 1 < len(self.my_list):
                self.differences_list.append(self.my_list[i + 1] - self.my_list[i])
                
        
        # Find the maximum pairs
        for j in range(len(self.differences_list)):
            for k in range(j ,len(self.differences_list)):
                self.sum_values = self._add_items(self.differences_list[j:k])

                if self.sum_values >= self.maximum_sum and sum(self.differences_list[j:k]) == self.sum_values:
                    self.maximum_sum = self.sum_values
                    self.pairs_indices.append((j,k-1,self.maximum_sum))
                # Reset the value of sum_values
                self.sum_values = 0
        
        return self.differences_list, self.pairs_indices, self.maximum_sum

def main():
    from random import randint
    random_list = []

    # print("Creating the random list")
    # for _ in range(100000):
    #     random_list.append(randint(-4500,6780))

    # print("Creating the Insertion Sort Object")
    # sorter = Insertion(random_list)
    
    # print("Beginning Ascending Sort - Insertion Sort")
    # print("Sorting in Ascending Order - Insertion Sort (In Progress)........")
    # print(sorter.ascending())
    # print("Done Sorting in Ascending Order")

    # print("Beginning Descending Sort - Insetion Sort")
    # print("Sorting in Descending Order - Insertion Sort (In Progress)........")
    # print(sorter.descending())
    # print("Done Sorting in Descending Order")

    for _ in range(40):
        random_list.append(randint(-200, 200))

    # sorter = Insertion(random_list)
    # print(sorter.ascending())
    
    sorter = BubbleSort(random_list)
    print(sorter.ascending())

    print("======================================================")
    print("=========== Deriving the maximum Sub Array ===========")
    print("======================================================")
    my_subarray = MaxSubArrayOne(random_list)
    diff_list, pairs_list, maxsum = my_subarray.max_subarray()

    print(f"\nTrading day prices:\n{random_list}")
    print(f"\nDifferences between contiguous days:\n{diff_list}")
    print(f"\nTuples of high subarray sum values:\n{pairs_list}")
    print(f"\nMaximum SubArray Value:\n{maxsum}")



main()