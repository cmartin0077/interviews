# Given an array of integers, find two numbers such that they add up to a specific target
# number.
# The function twoSum should return indices of the two numbers such that they add
# up to the target, where index1 must be less than index2. Please note that your returned
# answers (both index1 and index2) are not zero-based.
#
# For example:
# Input: numbers={2, 7, 11, 15}, target=9
#
# Output: index1=0, index2=1


def twoSum(numbers, target):
    # keep a dict of number:index as we go through the array
    saved_second_number = {}

    # go over each number
    # calculate the second number and fetch its index from te saved numbers in case we already found it
    for index, number in enumerate(numbers):
        second_number = target - number
        if second_number in saved_second_number:
            index1 = saved_second_number[second_number]
            index2 = index
            return (index1, index2)
        else:
            saved_second_number[number] = index


assert twoSum([2, 7, 11, 15], 9) == (0, 1)
assert twoSum([3, 2, 1, 10], 3) == (1, 2)
