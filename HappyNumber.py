# https://leetcode.com/problems/happy-number/


class HappyNumber:

    def __init__(self):
        pass

    @staticmethod
    def determine_if_number_is_happy(input_number):
        print("Original input number is: {0}.".format(input_number))
        is_happy = None
        answer = 0
        squared_set = set()

        if input_number <= 0:
            is_happy = False
        elif input_number == 1:
            is_happy = True
        else:
            while input_number > 1:

                answer = 0
                while input_number > 0:
                    print("Input number here is: {0}.".format(input_number))
                    remainder = (input_number % 10)
                    print("Remainder is: {0}.".format(remainder))
                    answer += ObjectHappyNumber.determine_square_of_a_number(remainder)
                    # answer += (remainder ** 2)
                    print("Answer is: {0}.".format(answer))
                    input_number = (input_number // 10)

                if answer in squared_set:
                    print("Answer is in Squared Set. Breaking...")
                    is_happy = False
                    break
                elif answer == 1:
                    is_happy = True
                    break
                else:
                    squared_set.add(answer)
                    print("Squared set is: {0}.".format(squared_set))
                    input_number = answer

        return is_happy

    @staticmethod
    def determine_square_of_a_number(number):
        squares_list = {0: 0,
                        1: 1,
                        2: 4,
                        3: 9,
                        4: 16,
                        5: 25,
                        6: 36,
                        7: 49,
                        8: 64,
                        9: 81}

        return squares_list[number]


ObjectHappyNumber = HappyNumber
# print(ObjectHappyNumber.determine_if_number_is_happy(0))
# print(ObjectHappyNumber.determine_if_number_is_happy(1))
# print(ObjectHappyNumber.determine_if_number_is_happy(2))
# print(ObjectHappyNumber.determine_if_number_is_happy(3))
# print(ObjectHappyNumber.determine_if_number_is_happy(4))
# print(ObjectHappyNumber.determine_if_number_is_happy(5))
# print(ObjectHappyNumber.determine_if_number_is_happy(6))
# print(ObjectHappyNumber.determine_if_number_is_happy(7))
# print(ObjectHappyNumber.determine_if_number_is_happy(10))
# print(ObjectHappyNumber.determine_if_number_is_happy(11))
print(ObjectHappyNumber.determine_if_number_is_happy(19))

# ObjectHappyNumber.determine_square_of_a_number(9)

