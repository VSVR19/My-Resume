# https://leetcode.com/problems/implement-strstr/


# class HaystackNeedle:
#
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def find_needle_haystack(haystack, needle):
#         result = -1
#         length_haystack = len(haystack)
#         length_needle = len(needle)
#         index_list = []
#         sender = 0
#
#         if length_haystack == 0 and length_needle == 0:
#             print("Over.")
#             result = 0
#         elif length_needle > length_haystack:
#             print("Here.")
#             result = -1
#         elif length_needle <= 0:
#             print("There.")
#             result = 0
#         else:
#             for number in range(length_haystack):
#                 if haystack[number] == needle[0]:
#                     # result = number
#                     index_list.append(number)
#                     # break
#
#             print("Index list is: {0}.".format(index_list))
#
#             for number in range(0, len(index_list)):
#                 result = index_list[number]
#                 print("Current result is: {0}.".format(result))
#
#                 flag = ObjectHaystackNeedle.traverse_haystack_needle(haystack, needle, length_needle, result, index_list)
#
#                 if flag:
#                     break
#
#                 if not flag:
#                     result = -1
#
#         print("*****Result is: {0}.*****".format(result))
#         # return result
#
#     @staticmethod
#     def traverse_haystack_needle(haystack, needle, length_needle, result, index_list):
#         print("In Traverse function.")
#         flag = False
#
#         for number in range(0, length_needle):
#             if haystack[result] == needle[number]:
#                 print("If 0.")
#                 result += 1
#                 fl
#             else:
#                 print("Else.")
#                 flag = False
#                 break
#
#             if result >= len(haystack) and number <= length_needle:
#                 print("If 1.")
#                 # flag = False
#                 break
#
#         print("Flag in Traverse is: {0}.".format(flag))
#
#         return flag
#
#
# ObjectHaystackNeedle = HaystackNeedle
# # ObjectHaystackNeedle.find_needle_haystack("hello", "ll")
# ObjectHaystackNeedle.find_needle_haystack("aaaaa", "aab")
# # ObjectHaystackNeedle.find_needle_haystack("aaa", "aaa")
# # ObjectHaystackNeedle.find_needle_haystack("aaa", "ccc")
# # ObjectHaystackNeedle.find_needle_haystack("aaa", "")
# # ObjectHaystackNeedle.find_needle_haystack("aaa", "aaaaaaaaaaaaaaaaaa")
# # ObjectHaystackNeedle.find_needle_haystack("", "")
# # ObjectHaystackNeedle.find_needle_haystack("mississippi", "issip")

class HaystackNeedle:

    def __init__(self):
        pass

    @staticmethod
    def find_needle_haystack(haystack, needle):
        length_haystack = len(haystack)
        length_needle = len(needle)

        if length_needle == 0:
            return 0

        for outer in range(0, ((length_haystack - length_needle) + 1)):
            for inner in range(0, length_needle):
                print("Outer is: {0}.".format(outer))
                print("Inner is: {0}.".format(inner))

                print(haystack[outer + inner], needle[inner])

                if haystack[outer + inner] != needle[inner]:
                    break

                if inner == (length_needle - 1):
                    return outer

        return -1


ObjectHaystackNeedle = HaystackNeedle
# print(ObjectHaystackNeedle.find_needle_haystack("hello", "ll"))
# print(ObjectHaystackNeedle.find_needle_haystack("aaaaa", "aab"))
# print(ObjectHaystackNeedle.find_needle_haystack("aaa", "aaa"))
# print(ObjectHaystackNeedle.find_needle_haystack("aaa", "ccc"))
# print(ObjectHaystackNeedle.find_needle_haystack("aaa", ""))
# print(ObjectHaystackNeedle.find_needle_haystack("aaa", "aaaaaaaaaaaaaaaaaa"))
# print(ObjectHaystackNeedle.find_needle_haystack("", ""))
print(ObjectHaystackNeedle.find_needle_haystack("ramana", "ana"))
