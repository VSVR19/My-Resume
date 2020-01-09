# https://leetcode.com/problems/two-sum/


class ArrayPair:

    def __init__(self):
        pass

    # @staticmethod
    # def calculate_target_pairs(number_list, target):
    #     old_number = 0
    #     result_list = []
    #     result_tuple = ()
    #
    #     index_list = []
    #     index_tuple = ()
    #
    #     for number in range(len(number_list)):
    #         result = target - number_list[number]
    #
    #         if result + old_number == target:
    #             # result_list.append(result)
    #             # result_list.append(old_number)
    #             result_tuple = (result, old_number)
    #             result_list.append(result_tuple)
    #
    #             if result == old_number:
    #                 index_tuple = (number_list.index(result), (number_list.index(old_number) + 1))
    #                 index_list.append(index_tuple)
    #             else:
    #                 index_tuple = (number_list.index(result), number_list.index(old_number))
    #                 index_list.append(index_tuple)
    #
    #             # index_list.append(number_list.index(result))
    #             # index_list.append(number_list.index(old_number))
    #
    #         old_number = result
    #         print("Result is: {0}.".format(result))
    #
    #     print("Result list is: {0}.".format(result_list))
    #     print("Index list is: {0}.".format(index_list))
    #     # return index_list

    # @staticmethod
    # def calculate_target_pairs(numeric_list, target):
    #     result_list = []
    #
    #     for number in range(len(numeric_list)):
    #         result = target - numeric_list[number]
    #         print("Result is: {}.".format(result))
    #
    #         if result in numeric_list:
    #             result_tuple = (numeric_list[number], result)
    #             print("Result tuple is: {0}.".format(result_tuple))
    #
    #             break
    #
    #     if numeric_list.index(numeric_list[number]) == numeric_list.index(result):
    #         # print([numeric_list.index(numeric_list[number]), numeric_list.index(result) + 1])
    #         result_list.append(numeric_list.index(numeric_list[number]))
    #         result_list.append(numeric_list.index(result) + 1)
    #
    #     else:
    #         # print([numeric_list.index(numeric_list[number]), numeric_list.index(result)])
    #         result_list.append(numeric_list.index(numeric_list[number]))
    #         result_list.append(numeric_list.index(result))
    #
    #     print("Result list is: {0}.".format(result_list))
        # return result_list

    @staticmethod
    # Input parameters are- A numeric list and the target to which two numbers in this array add up to.
    def calculate_target_pairs(number_list, target):
        # Declaring a dictionary to store
        # Numbers in the list as keys and their indexes as values.

        # The maximum size of this will be 'n'- the number of elements in the input list.
        # Remember, both key and value is one element.
        # Therefore, we have a SC of O(n) here.
        number_hash = {}

        # Loop through the input list to form a numbers: latest_indexes dictionaries.

        # We loop through 'n' elements of the input list.
        # Therefore, TC here is O(n).
        for number in range(len(number_list)):
            # If we encounter a number for the first time,
            # Add that number as a key.
            # And its index in the input list as value.
            if number_list[number] not in number_hash:
                number_hash[number_list[number]] = number_list.index(number_list[number])
            # If a number shows up again,
            # Add that number as a key. (the existing key will be overwritten)
            # Add the loop iterator as its value.
            # This will ensure that we take the latest index of a particular value in the input list.
            else:
                number_hash[number_list[number]] = number
                # number_hash[number_list[number]] = number_list.index(number_list[number])

        # Print the constructed dictionary.
        print("The dictionary is: {0}.".format(number_hash))

        # Once again, loop through the input list.
        for number in range(len(number_list)):
            # Subtract each element in the input list with the (input) target.
            complement_number = target - number_list[number]
            print("Complement is: {0}.".format(complement_number))

            # Check if the complement number is a key in the dictionary.
            # And check if the value of the complement number is not equal to the current loop iterator.
            # This is to ensure that, same number from the input list is not added twice;
            # And printed out as the final result.
            if complement_number in number_hash.keys() and number_hash[complement_number] != number:
                # Construct the result tuple.
                # Parameter 1- Current loop iterator.
                # Parameter 2- Value of the current key in the loop.
                # Its almost like Magic!
                result_tuple = (number, number_hash[complement_number])
                print(result_tuple)
                # Since there is bound to only one result in the input array, break exit the loop.
                break


ObjectArrayPair = ArrayPair
ObjectArrayPair.calculate_target_pairs([2, 7, 11, 15], 9)
# ObjectArrayPair.calculate_target_pairs([3, 3], 6)
# ObjectArrayPair.calculate_target_pairs([1, 3, 2, 2], 4)
# ObjectArrayPair.calculate_target_pairs([3, 2, 3], 6)
# ObjectArrayPair.calculate_target_pairs([2, 7, 11, 15], 9)
# ObjectArrayPair.calculate_target_pairs([3, 2, 4], 6)
# ObjectArrayPair.calculate_target_pairs([2, 2, 1, 3], 6)
# ObjectArrayPair.calculate_target_pairs([3, 2, 3], 6)
# ObjectArrayPair.calculate_target_pairs([1, 3, 2, 2], 4)
