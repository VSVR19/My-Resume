# This program finds the longest prefix in a list of words.
# This program has a TC of O(n).
# As for example, we might iterate over every character of every word in the input.
# This program has a SC of O(n).
# As we dont use any additional data structures.


class LongestCommonPrefix:

    def __init__(self):
        pass

    @staticmethod
    def display_longest_common_prefix(words_list):
        # The prefix letters will be appended to this string- letter by letter.
        longest_prefix = ""
        # Get the length of the word list.
        length_words_list = len(words_list)

        # Invalid input validation.
        if length_words_list <= 0:
            return longest_prefix

        # Get the first word of the input list.
        # This is used as a comparator and compared with all the other elements in the list.
        comparision_word = words_list[0]
        # An indexer.
        comparision_index = 0

        # Iterate letter by letter over the comparator- the first letter in the input list.
        for comparision_letter in comparision_word:
            print("Comparision letter is: {0}.".format(comparision_letter))

            # Now iterate over the remaining elements in the input list.
            # Note that the range starts from One so to exclude the 'comparator'.
            for inner_indexer in range(1, length_words_list):

                # Get the subsequent words one by one.
                current_word = words_list[inner_indexer]
                print("Current word is: {0}.".format(current_word))

                # What is this 'If' doing here?
                # This 'If' prevents an Array Out of Bounds exception.
                # We try to access a character in a current word
                # Before checking the length of the current word.
                # So, if we exceed the length, it means that
                # We have met the shortest word and there is no need to check for any more prefixes.

                if comparision_index >= len(current_word):
                    return longest_prefix

                # Get the letters in the subsequent words.
                # 'inner indexer' is not be used here- if used,
                # The iteration over individual words get tied to the length of the input list.
                current_letter = current_word[comparision_index]
                print("Current letter is: {0}.".format(current_letter))

                # Two conditions break this inner loop here:
                # If the letters from the comparator and the subsequent words are not equal
                # Or if the comparision index is greater than the length of the current word.
                if comparision_letter != current_letter or comparision_index > len(current_word):
                    return longest_prefix

            # Once the inner loop ends, increment the comparision index.
            # This will ensure that we move on to the next characters in the subsequent words.
            comparision_index += 1
            # Append the comparision letter to the result variable.
            longest_prefix += comparision_letter
            print("*****Longest prefix is: {0}*****".format(longest_prefix))

        return longest_prefix


ObjectLongestCommonPrefix = LongestCommonPrefix
print(ObjectLongestCommonPrefix.display_longest_common_prefix(["flower","flow","flight"]))
# print(ObjectLongestCommonPrefix.display_longest_common_prefix(["aa", "a"]))
