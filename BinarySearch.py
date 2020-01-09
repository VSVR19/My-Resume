# This class implements 'BinarySearch' technique and returns the index of an element in an array. (if present)
# A Classic TC analysis: logn
# SC analysis: Always a constant- O(1).
# https://hackernoon.com/what-does-the-time-complexity-o-log-n-actually-mean-45f94bb5bfbf
# https://leetcode.com/problems/binary-search/
class BinarySearch:

    def __init__(self):
        pass

    # A static method as arguments are directly passed to the method itself.
    @staticmethod
    def display_specified_number(numeric_list, target_number):
        # The below two variables specifies the boundaries of the input array.

        # Always consumes constant space.
        left_index = 0
        right_index = len(numeric_list) - 1
        flag = True


        # The left index must be always greater or equal to the right index.
        # This ensures that the array has at least one element.
        while left_index <= right_index:
            # Find the middle element of the array.

            # Always consumes constant space.
            middle_element = int((left_index + right_index) / 2)

            # If the middle element is equal to the target element, return the index and break- exit the method.
            if numeric_list[middle_element] == target_number:

                # Always consumes constant space.
                result_number = middle_element
                result = result_number
                # print("The element is present at the index: {0}.".format(result_number))
                flag = False
                break

            # If the middle element is less than the target number,
            # Ignore the left half of the input array by increasing the left index.
            elif numeric_list[middle_element] < target_number:

                # Always consumes constant space.
                left_index = middle_element + 1

            # If the middle element is greater than the target number,
            # Ignore the right half of the input array by decreasing the right index.
            elif numeric_list[middle_element] > target_number:

                # Always consumes constant space.
                right_index = middle_element - 1

        # If the control flow reaches here, it implies that the target element is not present in the input array.
        if flag:
            result = -1
            # print("The element is not present.")

        return result


ObjectBinarySearch = BinarySearch
# number_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
# number_list = [2, 3, 4, 10, 40]
number_list = [-1,0,3,5,9,12]
# number_list = [-1,0,3,5,9,12]

print(ObjectBinarySearch.display_specified_number(number_list, 9))


