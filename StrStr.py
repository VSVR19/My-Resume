class StrStr:

    def __init__(self):
        pass

    @staticmethod
    def search_needle_haystack(haystack, needle):
        # If the needle is not present in haystack, the result is -1.
        result = -1
        # Get the lengths of needle and haystack.
        needle_length = len(needle)
        print("Needle Length is: {0}.".format(needle_length))
        haystack_length = len(haystack)
        print("Haystack Length is: {0}.".format(haystack_length))

        # Result is zero if the length of needle is less than or equals zero.
        if needle_length <= 0:
            result = 0
        else:
            # Using Pointer1 and Pointer2, we create a 'bar' whose length equals the length of the needle.
            pointer1 = 0
            pointer2 = needle_length

            # The most interesting part- 'iterations'.
            # Iterations is the number of times we check for needle in the haystack.
            # For example, if the haystack is 'hello' and needle is 'll'.
            # We search: 'he', 'el', 'll', 'lo'.
            # For any combination of haystack and needle, iterations is obtained by subtracting both their lengths.
            iterations = (haystack_length - needle_length)
            print("Total Iterations: {0}.".format(iterations))

            # As explained above.
            # And, Pointer1 starts at 0
            # and Pointer2 starts at the index equal to the length of the needle.
            for pointer1 in range(iterations + 1):
                # Using the 'bar', create a substring in the haystack.
                substring = haystack[pointer1: pointer2]
                print("Substring is: {0}.".format(substring))

                # If this substring equals needle, Pointer1 is the index in haystack where the needle starts.
                if needle == substring:
                    # So the result equals Pointer1.
                    result = pointer1
                    break

                # Pointer1 gets auto-incremented by the for loop.
                # And here we increment Pointer2, so that for every iteration, the bar moves one index and reaches the end of the haystack.
                pointer2 += 1

        return result

ObjectStrStr = StrStr
# print(ObjectStrStr.search_needle_haystack("hello", "ll"))
# print(ObjectStrStr.search_needle_haystack("hello", "le"))
print(ObjectStrStr.search_needle_haystack("mississippi", "issip"))
