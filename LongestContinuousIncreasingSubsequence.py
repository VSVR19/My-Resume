# https://leetcode.com/problems/longest-continuous-increasing-subsequence/submissions/
# https://www.youtube.com/watch?v=dF5vBO4bbzs

# This program computes the longest increasing continuous subsequence in a sequence of numbers.
# This program has a TC of O(n) as
# We must loop through all the elements of the input array.
# This program has a SC of O(1) as
# A constant amount of memory is used, irrespective of the input.


class LongestContinuousIncreasingSubsequence:

    def __init__(self):
        pass

    @staticmethod
    def determine_length(input_sequence):
        # Initialize the maximum length to one.
        # Any array of size >= 1, will have at lest 1 continuous increasing subsequence.
        maximum_length = 1
        # A temporary variable.
        # This tells us the where the 'new' or 'next' subsequence starts.
        current = 1
        length_input_sequence = len(input_sequence)

        if length_input_sequence <= 0:
            maximum_length = 0
        else:
            # We start at 1 because we need to compare the element at index 1 to its previous element.
            # A similar comparision cannot be achieved with the element at index 0.
            for indexer in range(1, length_input_sequence):

                # The current element must be greater than than its previous element.
                if input_sequence[indexer] > input_sequence[indexer- 1]:
                    # If yes, increase the length of the subsequence.
                    current += 1
                else:
                    # No, reinitialize current to 1 and start a 'new' subsequence at this index.
                    current = 1

                # Whenever current is greater than maximum_length, maximum_length becomes current.
                if current > maximum_length:
                    # This ensures that the maximum length obtained till now is not lost whenever we start a new subsequence.
                    maximum_length = current

        return maximum_length


ObjectLongestContinuousIncreasingSubsequence = LongestContinuousIncreasingSubsequence
print(ObjectLongestContinuousIncreasingSubsequence.determine_length([4, 7, 1, 2, 3, 0]))
# print(ObjectLongestContinuousIncreasingSubsequence.determine_length([1, 3, 5, 4, 7]))
# print(ObjectLongestContinuousIncreasingSubsequence.determine_length([4, 7]))
# print(ObjectLongestContinuousIncreasingSubsequence.determine_length([2, 1]))
# print(ObjectLongestContinuousIncreasingSubsequence.determine_length([2, 2, 2, 2, 2]))
