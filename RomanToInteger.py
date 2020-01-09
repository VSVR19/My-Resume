# https://leetcode.com/problems/roman-to-integer/

# This program converts Roman numbers to Integers.
# This program has a TC of O(n).
# And a SC of O(1).
class RomanToInteger:

    def __init__(self):
        pass

    @staticmethod
    def convert_roman_to_integer(roman_number):
        # Get the length of the input.
        length_roman_number = len(roman_number)
        # A mapping of roman numerals to integers.
        conversion_dictionary = {'I': 1,
                                 'V': 5,
                                 'X': 10,
                                 'L': 50,
                                 'C': 100,
                                 'D': 500,
                                 'M': 1000
                                 }

        # First two variables to iterate the input, 'roman_number'.
        left_indexer = 0
        right_indexer = 1
        # Stores the rolling totals.
        result_number = 0

        # The right_indexer must always be in the bounds of the input.

        # Well' iterate through all the characters of the input string.
        # So we have a TC of O(n).
        while right_indexer <= length_roman_number:
            # First, extract the letter from the input string.

            # We are accessing a particular element.
            # So its a Constant Time operation.
            left_letter = roman_number[left_indexer]
            print("Left letter is: {0}.".format(left_letter))

            # Next, extract the letters' value from the dictionary.

            # Again, a Constant Time operation.
            left_value = conversion_dictionary[left_letter]
            print("Left value is: {0}.".format(left_value))

            # Almost a 'base case'!
            # If right_indexer gets beyond the limits of the input string,
            # Add left value to the result and break- exit the loop.

            # Again, a Constant Time operation.
            if right_indexer >= length_roman_number:
                result_number += left_value
                break

            # Similarly, extract the 'right' letter from the input string.

            # Again, a Constant Time operation.
            right_letter = roman_number[right_indexer]
            print("Right letter is: {0}.".format(right_letter))

            # Extract the value of the right letter from the dictionary.

            # Again, a Constant Time operation.
            right_value = conversion_dictionary[right_letter]
            print("Right value is: {0}.".format(right_value))

            # Now compare left and right values.
            # If the left value is greater or equal to the right value,
            # Add the left value to result
            # And move both the pointers by one.

            # Again, a Constant Time operation.
            if left_value >= right_value:
                result_number += left_value
                left_indexer += 1
                right_indexer += 1

            # If left value is less than right value,
            # Add to result the difference between left and right values
            # And move both the pointers by two indices.

            # Again, a Constant Time operation.
            elif left_value < right_value:
                result_number += right_value - left_value
                left_indexer += 2
                right_indexer += 2

            print("*****Result number is: {0}*****".format(result_number))

        print("*****Final result number is: {0}*****".format(result_number))

        return result_number


ObjectRomanToInteger = RomanToInteger
# ObjectRomanToInteger.convert_roman_to_integer('LVIII')
# ObjectRomanToInteger.convert_roman_to_integer('MCMXCIV')
# ObjectRomanToInteger.convert_roman_to_integer('IX')
# ObjectRomanToInteger.convert_roman_to_integer('IV')
ObjectRomanToInteger.convert_roman_to_integer('DCXXI')
