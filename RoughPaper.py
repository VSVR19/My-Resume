class RoughPaper:

    def __init__(self):
        pass

    @staticmethod
    def single_number(nums):
        counting_dictionary = {}

        for number in nums:
            try:
                counting_dictionary.pop(number)
            except:
                counting_dictionary[number] = 1

        return counting_dictionary.popitem()[0]

    @staticmethod
    def rotate_array(number_list, rotations):
        length_number_list = len(number_list)
        target = rotations % length_number_list

        ObjectRoughPaper.rotate_partial_array(number_list, 0, length_number_list - 1)
        # print("Input after First rotation: {0}.".format(number_list))

        ObjectRoughPaper.rotate_partial_array(number_list, 0, target - 1)
        # print("Input after Second rotation: {0}.".format(number_list))

        ObjectRoughPaper.rotate_partial_array(number_list, target, length_number_list - 1)
        # print("Input after Third rotation: {0}.".format(number_list))

    @staticmethod
    def rotate_partial_array(number_list, start, end):
        while start < end:
            temp = number_list[start]
            number_list[start] = number_list[end]
            number_list[end] = temp

            start += 1
            end -= 1

            # print("Progress information: {0}.".format(number_list))

    @staticmethod
    def solve_two_sum(input_array, target):
        counting_dictionary = {}

        for number in range(len(input_array)):
            counting_dictionary[input_array[number]] = number

            complement_number = (target - input_array[number])

            if complement_number in counting_dictionary and input_array.index(complement_number) != number:
                return number, input_array.index(complement_number)

        # for number in range(len(input_array)):


    # @staticmethod
    # def solve_two_sum(input_array, target):
    #     counting_dictionary = {}
    #
    #     for number in range(len(input_array)):
    #         counting_dictionary[input_array[number]] = number
    #
    #     for number in range(len(input_array)):
    #         complement_number = (target - input_array[number])
    #
    #         if complement_number in counting_dictionary and input_array.index(complement_number) != number:
    #             return number, input_array.index(complement_number)


ObjectRoughPaper = RoughPaper
# ObjectRoughPaper.single_number([4, 1, 2, 1, 2])
# ObjectRoughPaper.rotate_array([1, 2, 3, 4, 5, 6, 7], 3)
# ObjectRoughPaper.rotate_array([-1, -100, 3, 99], 2)
# print(ObjectRoughPaper.solve_two_sum([2, 7, 11, 15], 9))
# print(ObjectRoughPaper.solve_two_sum([3, 3], 6))
# print(ObjectRoughPaper.solve_two_sum([3, 2, 3], 6))
# print(ObjectRoughPaper.solve_two_sum([3, 2, 4], 6))
print(ObjectRoughPaper.solve_two_sum([-1, -2, -3, -4, -5], -8))


# print(ObjectRoughPaper.solve_two_sum([2, 2, 1, 3], 6))
# print(ObjectRoughPaper.solve_two_sum([1, 3, 2, 2], 4))
