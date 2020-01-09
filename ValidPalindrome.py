# https://leetcode.com/problems/valid-palindrome/
# This program determines if the input string is a palindrome.
# Since we traverse all the characters in the input string,
# This program has a TC of O(n).
# Since the comparision of elements are made in-place and no additional data structures are used,
# This program has a SC of O(1).


class ValidPalindrome:

    def __init__(self):
        pass

    @staticmethod
    def check_palindrome(sentence):
        # Get the length of the input string.
        length_sentence = (len(sentence) - 1)
        # Calculate the floor of the length of input string divided by two.
        mid_sentence = (length_sentence // 2)
        # A counter variable which will be explained below.
        mid_sentence_counter = 0
        # Two more counter variables.
        # Start Counter is used to traverse the string left to right.
        start_counter = 0
        # End Counter is used to traverse the string right to left.
        end_counter = 0
        # As always, a cute and lovely flag variable.
        flag = True

        # Start looping through the input string.
        for indexer in range(length_sentence):
            print("Indexer is: {0}.".format(indexer))
            # Get the first letter of the input string.
            start_letter = sentence[start_counter].lower()
            # Get the last letter of the input string.
            end_letter = sentence[length_sentence - end_counter].lower()

            # If start_letter is neither alphabet nor number,
            if not start_letter.isalnum():
                print("Here")
                # Increment start counter by one.
                start_counter += 1
                # And get the next letter from the left of the input string.
                start_letter = sentence[start_counter].lower()

            # If end_letter is neither alphabet nor number,
            elif not end_letter.isalnum():
                print("There")
                # Increment end counter by one.
                end_counter += 1
                # And get the next letter from the right of the input string.
                end_letter = sentence[length_sentence - end_counter].lower()

            # The above 'statements' raise one obvious question.
            # What if the 'next' letter is also not alphanumeric?
            # We ignore all the non alphanumeric characters.
            # And perform a comparision only when both start and end letters are alphanumeric.
            # We effectively compare only alphanumeric characters.
            if start_letter.isalnum() and end_letter.isalnum():
                print("Start letter is: {0}.".format(start_letter))
                print("End letter is: {0}.".format(end_letter))
                # Every start and end letters, now that they are alphanumeric,
                # Must be equal.
                # If they are not equal, break-exit the loop.
                if start_letter != end_letter:
                    flag = False
                    break
                start_counter += 1
                end_counter += 1

            # This part is inspired from the Binary Search algorithm.
            # For any input string, the number of comparisons required will be floor(length / 2).
            # Once that many comparisons are made, we can break-exit the main For loop.
            if mid_sentence_counter == mid_sentence:
                break

            # Incrementation to keep track of the number of comparisons made.
            mid_sentence_counter += 1

        if flag:
            print("*****Valid Palindrome.*****")
        else:
            print("*****Invalid Palindrome.*****")

        # print(flag)
        # return flag


ObjectValidPalindrome = ValidPalindrome
ObjectValidPalindrome.check_palindrome("A man, a plan, a canal: Panama")
# ObjectValidPalindrome.check_palindrome("race a car")
# ObjectValidPalindrome.check_palindrome("Malayalam")
# ObjectValidPalindrome.check_palindrome("Anna")
# ObjectValidPalindrome.check_palindrome("ab")
# ObjectValidPalindrome.check_palindrome("aa")
# ObjectValidPalindrome.check_palindrome("ab2a")
# ObjectValidPalindrome.check_palindrome("Sore was I ere I saw Eros.")
