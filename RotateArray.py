# # https://leetcode.com/problems/rotate-array/
#
# class RotateArray:
#
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def reverse_array(input_list, start, mid, end):
#         print("Enter")
#         counter = 0
#         for number in range(mid):
#             temp = input_list[end - 1 - counter]
#             input_list[end - 1 - counter] = input_list[start]
#             input_list[start] = temp
#
#             start += 1
#             counter += 1
#
#             print(input_list)
#
#     @staticmethod
#     def prepare_input_array(input_list, rotations):
#         len_input_list = len(input_list)
#
#         if rotations > len_input_list:
#             print("Subtracted!")
#             rotations = rotations - len_input_list
#
#         if len_input_list >= 2 and rotations >= 0:
#             ObjectRotateArray.reverse_array(input_list, 0, (len_input_list // 2), len_input_list)
#             ObjectRotateArray.reverse_array(input_list, 0, (rotations - 1), rotations)
#             ObjectRotateArray.reverse_array(input_list, rotations, ((len_input_list - rotations) // 2), len_input_list)
#
#
# ObjectRotateArray = RotateArray
# # ObjectRotateArray.prepare_input_array([1, 2, 3, 4, 5, 6, 7], 3)
# # ObjectRotateArray.prepare_input_array([-1,-100,3,99], 2)
# # ObjectRotateArray.prepare_input_array([-1], 2)
# # ObjectRotateArray.prepare_input_array([1, 2], 3)
# ObjectRotateArray.prepare_input_array([1, 2, 3, 4, 5], 4)


# class Solution:
#
#     @staticmethod
#     def rotate(input_list, target):
#         target = target % len(input_list)
#         print("Target is: {0}.".format(target))
#
#         Solution.reverse(input_list, 0, (len(input_list) - 1))
#         Solution.reverse(input_list, 0, (target - 1))
#         Solution.reverse(input_list, target, (len(input_list) - 1))
#
#     @staticmethod
#     def reverse(input_list, start, end):
#         while start < end:
#             print("Enter")
#             temp = input_list[start]
#             input_list[start] = input_list[end]
#             input_list[end] = temp
#
#             start += 1
#             end -= 1
#
#             print(input_list)
#
#
# ObjectSolution = Solution
# # ObjectSolution.rotate([1, 2, 3, 4, 5, 6, 7], 3)
# ObjectSolution.rotate([-1, -100, 3, 99], 2)
# # ObjectSolution.rotate([1, 2], 3)
# # ObjectSolution.rotate([1, 2, 3, 4, 5], 4)

# This class rotates an numeric array by 'target' times.
# This program has a TC of O(n).
# This program has a SC of O(1) a.k.a 'Constant Space'.

class RotateArray:

    def __init__(self):
        pass

    @staticmethod
    def rotate(input_list, target):
        # Get the length of the input list.
        input_list_length = len(input_list)
        # The magic step.
        # If the length of the input list is greater than target, the modulo operation will return target.
        # However, if length of input list is less than target, modulo operation returns the difference between them.
        # If the target and length are same, modulo will return zero, i.e, there is no need to rotate the array!
        target = target % input_list_length

        # Reverse the entire list.
        ObjectRotateArray.rotate_input_list(input_list, 0, (input_list_length - 1))
        # Sort the reversed input list from zeroth index till target - 1.
        ObjectRotateArray.rotate_input_list(input_list, 0, (target - 1))
        # Sort the reversed input list from target index till length of list - 1.
        ObjectRotateArray.rotate_input_list(input_list, target, (input_list_length - 1))

    @staticmethod
    def rotate_input_list(input_list, start, end):
        # This reverse routine is the one that should be followed.
        # This routine uses no 'mid'; works just with start and mid.
        while start < end:
            # print("Enter")
            # Get the first element.
            temp = input_list[start]
            # Get the last element and store it in the place of first element.
            input_list[start] = input_list[end]
            # Store the first element as the last element.
            input_list[end] = temp

            # Loop controls.
            start += 1
            end -= 1

            print(input_list)


ObjectRotateArray = RotateArray
# ObjectRotateArray.receive_input([1, 2, 3, 4, 5], 4)
