# Gaussian Number Summation

# If I want to add all numbers till a certain point, take an
# example till 4 { 1 + 2 + 3 + 4 } it can be easy to do
# the math in your head if the number is small, but what about 
# adding all numbers till 10,000? That brings us to Gaussian 
# Number Summation which says:
#  
# ((number_of_items) x (sum_of_pairs))/2
#  
# 1 2 3 4 => (number_of_items= 4)
# 4 3 2 1
#---------
# 5 5 5 5  => (sum_of_pairs = 5)

# 1 2 3 4 5 6  (number_of_items = 4)
# 6 5 4 3 2 1
# ------------
# 7 7 7 7 7 7 => (sum_of_pairs = 5)

#  1  2  3  4  5   6   7  8  9  (number_of_items = 4)
#  9  8  7  6  5   4   3  2  1
# ----------------------------
# 10 10 10 10 10  10 10  10 10  => (sum_of_pairs = 5)

#  OBSERVATION
# -------------
# Every single time the sum_of_pairs = (number_of_items + 1)
# therefore for us to add sequence numbers we'll use the below format
# 
# ( number_of_items * (number_of_items + 1) ) / 2
# or
# (1/2 x number_of_items x sum_of_pairs) 

#TODO: Implement the below operation.
def gaussian_summation(number_of_items):
    # Steps to follow
    # 
    # > Delete the word pass
    # > Make this function a return function.
    # > Write the code needed to implement the below operation
    #
    # number_of_items X number_of_items + 1
    # -------------------------------------
    #              2
    pass