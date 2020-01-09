# https://leetcode.com/problems/hamming-distance/solution/

# This program calculates the 'hamming distance' between two numbers.
# This program has a TC of O(1) as
# ???????????????????????????????
# This program has a SC of O(1) as
# As a constant amount of memory is used, regardless of the input.

class HammingDistance:

    def __init__(self):
        pass

    @staticmethod
    def determine_hamming_distance(number_one, number_two):
        binary_number_one = "{0: b}".format(number_one)
        binary_number_two = "{0: b}".format(number_two)

        binary_number_one = int(binary_number_one)
        binary_number_two = int(binary_number_two)

        counter = 0

        while binary_number_one > 0 and binary_number_two > 0:
            print("Here")

            digit_binary_number_one = (binary_number_one % 10)
            digit_binary_number_two = (binary_number_two % 10)

            if digit_binary_number_one != digit_binary_number_two:
                counter += 1

            binary_number_one = (binary_number_one // 10)
            binary_number_two = (binary_number_two // 10)

            print(binary_number_one, binary_number_two)

        print("Counter is: {0}.".format(counter))

        if binary_number_one > 0:
            while binary_number_one > 0:
                last_digit = (binary_number_one % 10)

                if last_digit == 1:
                    counter += 1

                binary_number_one = (binary_number_one // 10)

        elif binary_number_two > 0:
            while binary_number_two > 0:
                last_digit = (binary_number_two % 10)

                if last_digit == 1:
                    counter += 1

                binary_number_two = (binary_number_two // 10)

        print("Counter is: {0}.".format(counter))

    @staticmethod
    def determine_hamming_distance_bit_manipulation(number_one, number_two):
        # The variable which will hold the hamming distance.
        hamming_distance = 0

        while number_one > 0 or number_two > 0:
            print("Number one is: {0}.".format(number_one))
            print("Number two is: {0}.".format(number_two))

            # This modulo avoids us to convert a number to binary.
            # With each modulo operation, we get the right-most digit of the number in binary format!
            digit_number_one = number_one % 2
            print("Digit number one is: {0}.".format(digit_number_one))
            digit_number_two = number_two % 2
            print("Digit number two is: {0}.".format(digit_number_two))

            # XOR the right-most digits of both the input numbers.
            # The XOR truth table is really simple.
            # If digits are same, XOR will provide you zero.
            # If the digits are different, XOR will provide you one.
            xor_result = digit_number_one ^ digit_number_two
            print("XOR result is: {0}.".format(xor_result))

            # Add the total to the hamming distance.
            hamming_distance += xor_result

            # The most interesting part:
            # Right shift is nothing but pushing all the digits to the right by how many ever steps we need.
            # And since we modulo by 2, a last digit of 1, will provide us 1
            # And a last digit of 0 will provide us 0.
            # And, we are getting the bits we need.
            number_one = number_one >> 1
            print("Number one after shifting: {0}.".format(number_one))

            number_two = number_two >> 1
            print("Number two after shifting: {0}.".format(number_two))
            print("**********")

        return hamming_distance


ObjectHammingDistance = HammingDistance
# ObjectHammingDistance.determine_hamming_distance(1, 4)
# print(ObjectHammingDistance.determine_hamming_distance_bit_manipulation(1, 4))
# print(ObjectHammingDistance.determine_hamming_distance_bit_manipulation(1, 5))
print(ObjectHammingDistance.determine_hamming_distance_bit_manipulation(1, 32))
