# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/82271/Solution-with-three-follow-ups

class IntersectionOfTwoArrays:

    def __init__(self):
        pass

    @staticmethod
    def find_intersection_of_two_arrays(array_one, array_two):
        counting_dictionary = {}
        result_list = []

        for number in array_one:
            if number not in counting_dictionary:
                counting_dictionary[number] = 1
            else:
                counting_dictionary[number] += 1

        print(counting_dictionary)

        for number in array_two:
            if number in counting_dictionary and counting_dictionary[number] >= 1:
                result_list.append(number)
                counting_dictionary[number] -= 1

        print("Counting dictionary is: {0}.".format(counting_dictionary))
        print("Result list is: {0}.".format(result_list))


ObjectIntersectionOfTwoArrays = IntersectionOfTwoArrays
ObjectIntersectionOfTwoArrays.find_intersection_of_two_arrays([1, 2, 2, 1], [2, 2])
# ObjectIntersectionOfTwoArrays.find_intersection_of_two_arrays([4, 9, 5], [9, 4, 9, 8, 4])
