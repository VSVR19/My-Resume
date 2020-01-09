# https://leetcode.com/problems/to-lower-case/
class Solution:

    @staticmethod
    def toLowerCase(word):
        result_list = []
        if len(word) <= 0:
            return "Word Length must be greater than 0."
        else:
            for num in range(len(word)):
                upper_unicode_value = ord(word[num])
                lower_unicode_value = upper_unicode_value + 32

                if 97 <= lower_unicode_value <= 122:
                    result_list.append(chr(lower_unicode_value))
                else:
                    result_list.append(word[num])

            return "".join(result_list)


ObjectSolution = Solution
print(ObjectSolution.toLowerCase("H HM"))
