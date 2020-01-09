# https://leetcode.com/problems/sqrtx/


# class SquareRoot:
#
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def mySqrt(number):
#
#         if number == 0:
#             square_root = 0
#
#         else:
#             square_list = []
#             result = 1
#             num = 1
#
#             while result <= number:
#                 result = num * num
#                 square_list.append(result)
#
#                 result += 1
#                 num += 1
#
#             print(square_list)
#
#             square_root = ObjectSquareRoot.perform_binary_search(square_list, number)
#         print("*****Square root is: {0}*****.".format(square_root))
#
#     @staticmethod
#     def perform_binary_search(square_list, number):
#         left_index = 0
#         right_index = len(square_list) - 1
#         flag = True
#
#         while left_index <= right_index:
#             middle_element = (left_index + right_index) // 2
#
#             if square_list[middle_element] == number:
#                 flag = False
#                 break
#
#             elif square_list[middle_element] < number:
#                 left_index = middle_element + 1
#
#             elif square_list[middle_element] > number:
#                 right_index = middle_element - 1
#
#         if flag:
#             square_root = left_index
#         else:
#             square_root = left_index + 1
#
#         return square_root
#
#
# ObjectSquareRoot = SquareRoot
# ObjectSquareRoot.mySqrt(4)
# ObjectSquareRoot.mySqrt(8)
# ObjectSquareRoot.mySqrt(16)
# # ObjectSquareRoot.mySqrt(0)
# # ObjectSquareRoot.mySqrt(575316505)
# ObjectSquareRoot.mySqrt(1183321020)
# This is beyond Science!
# https://leetcode.com/problems/sqrtx/
# https://www.youtube.com/watch?v=VYtEKhxKd1Q&feature=youtu.be
# This calculates the nearest square root of a given number by using Binary Search.
# https://leetcode.com/problems/sqrtx/
# This program returns the square root of a input number.
# In one sentence, the TC of this program is:
# "o(logn)- 'cause with every loop, we have halved our data-set!"
# SC is always O(1) as we have not used any additional data structures.
# https://www.youtube.com/watch?v=VYtEKhxKd1Q&feature=youtu.be
class SquareRoot:

    def __init__(self):
        pass

    @staticmethod
    def mySqrt(number):
        # Initialize left and right for Binary Search.
        left = 1
        # Remember, right is not len(input array) - 1; its the given input number.
        right = number

        # Square roots of 0 and 1 are 0 and 1 respectively.
        if number <= 1:
            square_root = number
        else:
            while left < right:
                # Seems this is the midpoint formula.
                # Performing (right - 1) - left // 2 raises a TimeOut error.
                mid = left + (right - left) // 2
                print("Mid is:{0}.".format(mid))
                # Square the mid for faster processing time.
                squared_mid = mid * mid

                # If squared_mid equals the input number, it means that the number is a perfect square.
                # The mid is the inputs' square root and as a result, we return it.
                if squared_mid == number:
                    square_root = mid
                    return square_root

                # From the next number of mid,
                # Ignore the entire right half of the 'imaginary' array from 1 till the input number.
                # Why no 'mid + 1' as in the below 'elif' ?
                # 'Cause we are not checking '>='; its just '>' and hence,
                # Everything from 'mid + 1' can be ignored.
                elif squared_mid > number:
                    right = mid

                # Here, its less.
                # That means the mid itself is less.
                # So including mid, ignore the entire left half of the array.
                elif squared_mid < number:
                    left = mid + 1

            # If we reach here, it means that the input number is a not a perfect square.
            # Since we are rounding down, subtracting one from the 'left' will provide us the 'rounded down' SR.
            square_root = (left - 1)

        return square_root


ObjectSquareRoot = SquareRoot
print(ObjectSquareRoot.mySqrt(8))
# print(ObjectSquareRoot.mySqrt(16))
# print(ObjectSquareRoot.mySqrt(1183321020))
# print(ObjectSquareRoot.mySqrt(9))
# print(ObjectSquareRoot.mySqrt(3))

