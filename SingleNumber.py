# https://leetcode.com/problems/single-number/


class SingleNumber:

    def __init__(self):
        pass

    @staticmethod
    def display_single_number(number_list):

        if len(number_list) <= 0:
            flag = False
        else:

            result_dict = {}

            for number in number_list:
                try:
                    result_dict.pop(number)
                except:
                    result_dict[number] = 1
        if flag:
            return result_dict.popitem()[0]


ObjectSingleNumber = SingleNumber()
print(ObjectSingleNumber.display_single_number([2, 2, 1]))
