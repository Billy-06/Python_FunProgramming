"""
    Theta(n)     => both upper and lower bound
    O(n)         => Asymptotic Upper bound
    o(n)         => Non-tight Asymptotic Upper bound
    Omega(n)     => Asymptotic Lower bound
    w(n)         => Non-tight Asymptotic Lower bound

    Static Arrays: Static arrays are initiated with a fixed size in memory. By default python is
                    implements Dynamic arrays but in languages such as C++ and C# ( the Array
                    implementation has a fixed size data structure which means once created, we
                    can't thereafter append, or as the wording is in C++ & C#, push items into
                    the array (if we do the array get reinitialise and assigned new memory spaces that
                    adequately accomodate the new size). It goes without saying that we're 
                    contrained (and will also incur a higher cost) when using the static
                    Array data type, this is because we wouldn't be able to make insertions in runtime
                    or simply at will without the space in memory having to be reassigned all over 
                    again. insertions & deletion will O(n) due to the reassignment of memory
                    
    Dynamic Arrays: Dynamic Arrays are initiated with O(n) time size if the array will contain
                    n items. This creates room for the array to expand and with by quite a few
                    operations before needing to reallocate more memory. Dynamic arrays also
                    allow insertion both at runtime and at will which makes for a convenient
                    data structure for certain operations.

"""

class StaticArray:
    def __init__(self, n): self.data = [None] * n
    def get_at(self, index):
        # Raise and index error if the index value passed is 
        # not between 0..n else return the data at position 
        # index 
        if not (0 <= index < len(self.data)): raise IndexError
        return self.data[index]

    def set_at(self, index, value):
        # Raise and index error if the index value passed is 
        # not between 0..n else set the value of the item at
        # position index to value
        if not (0 <= index < len(self.data)): raise IndexError
        self.data[index] = value

def dob_match(students):
    n = len(students)
    record = StaticArray(n)
    for k in range(n):
        (name_one, dob_one) = students[k]
        for i in range(k):
            (name_two, dob_two) = record.get_at(i)
            if dob_one == dob_two: return (name_one, name_two)

        record.set_at(k, (name_one, dob_one))

    return None