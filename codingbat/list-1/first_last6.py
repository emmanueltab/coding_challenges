# Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

# first_last6([1, 2, 6]) → True
# first_last6([6, 1, 2, 3]) → True
# first_last6([13, 6, 1, 2, 3]) → False


def first_last(list):
    if(list[0] == 6 or list[-1] == 6):
        print("True")
    else:
        print("False")

list1 = [1, 5, 6]
list2 = [1, 1, 1]
first_last(list1)