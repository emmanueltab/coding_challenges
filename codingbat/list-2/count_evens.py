# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0


def count_evens(list):
        total = 0
        for num in list:
            if num % 2 == 0:
        return total

l1 = [2, 1, 2, 3, 4] #3
l2 = [2, 2, 0] #3
l3 = [1, 3, 5] # 0

print(count_evens(l3))
