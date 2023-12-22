# Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

# first_last6([1, 2, 6]) → True
# first_last6([6, 1, 2, 3]) → True
# first_last6([13, 6, 1, 2, 3]) → Fals

def first_last6(list):
    if(list[0] == 6 or list[-1] == 6):
        return(True)
    else:
        return(False)

list1 = [1, 5, 6]
list2 = [1, 1, 1]
full_list = [list1, list2]

for l in full_list:
        print(first_last6(l))
