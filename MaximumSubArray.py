# https://leetcode.com/problems/maximum-subarray/
# https://www.youtube.com/watch?v=2MmGzdiKR9Y
# https://github.com/bephrem1/backtobackswe/blob/master/Dynamic%20Programming%2C%20Recursion%2C%20%26%20Backtracking/MaxContiguousSubarraySum/MaxContiguousSubarraySum.java

# This program prints the largest possible sub-array sum in a numeric array.
# This program has a TC of O(n) as
# We traverse through all the elements of the input array.
# This program has a SC of O(1) as
# We do not use any additional data structures.
import sys


class MaximumSubArray:

    def __init__(self):
        pass

    # This is the O(n ^ 2) approach which times out on leetcode.com
    @staticmethod
    def detect_max_sub_array(input_array):
        length_input_array = len(input_array)
        result = -sys.maxsize - 1
        # print(result)

        if length_input_array <= 0:
            result = 0
        elif length_input_array == 1:
            result = input_array[0]
        else:
            for outer_indexer in range(length_input_array):
                addition_result = 0
                for inner_indexer in range(outer_indexer, length_input_array):
                    addition_result += input_array[inner_indexer]
                    # print("Addition result is: {0}.".format(addition_result))
                    
                    if addition_result >= result:
                        result = addition_result
                    # result = max(result, addition_result)

                # print("**********")
                # print("Result is: {0}.".format(result))
                # print("**********")

        return result

    # This is the preferred approach.
    @staticmethod
    def print_sum_max_sub_array(input_array):
        # Get the length of the input array.
        length_input_array = len(input_array)
        # Assign the below two variables to the first element in the input array.
        maximum_so_far = input_array[0]
        maximum_end_here = input_array[0]

        # Return the first element itself if the array has only one element.
        if length_input_array == 1:
            maximum_so_far = input_array[0]
        else:
            # Start looping from the second element of the input array.
            for indexer in range(1, length_input_array):
                # Check if the above maximum_end_here is greater on its own
                # Or becomes even larger by adding the next element.
                maximum_end_here = max((maximum_end_here + input_array[indexer]), input_array[indexer])
                # Get the maximum of the above result for every iteration.
                maximum_so_far = max(maximum_end_here, maximum_so_far)

        return maximum_so_far


ObjectMaximumSubArray = MaximumSubArray
# print(ObjectMaximumSubArray.detect_max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))
# print(ObjectMaximumSubArray.detect_max_sub_array([1,-5]))
# print(ObjectMaximumSubArray.detect_max_sub_array([1]))

# print(ObjectMaximumSubArray.print_sum_max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))
# print(ObjectMaximumSubArray.print_sum_max_sub_array([1,-5]))
# print(ObjectMaximumSubArray.print_sum_max_sub_array([-2, -1]))
print(ObjectMaximumSubArray.print_sum_max_sub_array([1, 2]))