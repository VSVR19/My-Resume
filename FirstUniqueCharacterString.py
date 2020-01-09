# https://leetcode.com/problems/first-unique-character-in-a-string/


class FirstUniqueCharacterInAString:

    def __init__(self):
        pass

    @staticmethod
    def find_first_unique_character(input_string):
        # print("Length of the input string is: {0}.".format(len(input_string)))
        flag = False
        result = -1

        if len(input_string) <= 0:
            result = -1
        else:
            counting_dictionary = {}

            for letter in input_string:
                if letter not in counting_dictionary:
                    counting_dictionary[letter] = 1
                else:
                    counting_dictionary[letter] += 1

            print(counting_dictionary)

            for key, value in counting_dictionary.items():
                if counting_dictionary[key] == 1:
                    flag = True
                    break

            if flag:
                result =  input_string.index(key)

        return result


ObjectFirstUniqueCharacterInAString = FirstUniqueCharacterInAString
# print(ObjectFirstUniqueCharacterInAString.find_first_unique_character("loveleetcode"))
# print(ObjectFirstUniqueCharacterInAString.find_first_unique_character("lv"))
# print(ObjectFirstUniqueCharacterInAString.find_first_unique_character(""))
print(ObjectFirstUniqueCharacterInAString.find_first_unique_character("cc"))