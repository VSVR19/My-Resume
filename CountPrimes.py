# https://leetcode.com/problems/count-primes/
# This class returns the number of prime number present upto to a specified range.
# This program has a TC of I DUNNO.
# This program has a SC of O(n).
import math


class CountPrimes:

    def __init__(self):
        pass

    @staticmethod
    def display_primes(target):

        # No prime numbers exist from any number less than and equal to zero.
        # Hence return zero.
        if target <= 1:
            output = 0
        else:
            # Create a list with number of Trues equal to the target.
            result_list = [True] * target
            len_result_list = len(result_list)
            print("Result list is:")
            print(result_list)

            # Get the square root of the target element.
            squared_target = int(math.sqrt(target))
            print("Squared target is: {0}.".format(squared_target))

            # The first for loop provides 'number1'.
            # This loop will run till sqrt(target)-- an optimization step.
            # This will prevent us checking every number in the list.
            for number1 in range(2, (squared_target + 1)):
                # The second for loop provides 'number2'.
                # However, this loop will run to its logical end- target.
                for number2 in range(number1, target):
                    # Multiply the numbers provided by the above two loops.
                    result = number1 * number2

                    # This condition ensures that the inner loop never runs to its logical end.
                    # If result exceeds the length of input list,
                    # It means that were' looking for numbers outside the list.
                    # So break- exit the list.
                    if result >= len_result_list:
                        break

                    # If result is in the input list, make it False.
                    if result_list[result]:
                        result_list[result] = False

            # Find the number of Trues in the input list.
            # Subtract the count by 2 as we have extra Trues at indices zero and one of the input list.
            output = result_list.count(True) - 2

        return output


ObjectCountPrimes = CountPrimes
print(ObjectCountPrimes.display_primes(1500000))
