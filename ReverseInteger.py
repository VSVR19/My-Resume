import math


class ReverseInteger:

    def __init__(self):
        pass

    @staticmethod
    def reverse_integer(number):
        negative_flag = False
        multiplier = 10
        final_result = 0

        if abs(number) != number:
            negative_flag = True
            number = abs(number)

        if number >= 2147483648 or number <= -2147483649:
            flag = False

        else:
            if number == 0:
                final_result = number
            else:
                number_of_digits = math.floor(math.log(number, 10))

                while number > 0:
                    remainder = number % 10
                    result = remainder * (multiplier ** number_of_digits)
                    final_result = result + final_result

                    number = number // 10
                    number_of_digits -= 1

                if negative_flag:
                    final_result *= -1

        if final_result >= 2147483648 or final_result <= -2147483649:
            final_result = 0

        print("Final Result is: {0}.".format(final_result))
        # return final_result


ObjectReverseInteger = ReverseInteger()
# ObjectReverseInteger.reverse_integer(-619)
# ObjectReverseInteger.reverse_integer(619)
# ObjectReverseInteger.reverse_integer(120)
# ObjectReverseInteger.reverse_integer(104)
# ObjectReverseInteger.reverse_integer(200)
# ObjectReverseInteger.reverse_integer(00)
ObjectReverseInteger.reverse_integer(1534236469)
