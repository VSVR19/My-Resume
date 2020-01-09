# https://leetcode.com/problems/pascals-triangle/
# https://www.youtube.com/watch?v=7pOzP9m_bX8
# This program prints the 'Pascals' Triangle' up to and including the input number.
# This program has a TC of O(n ^ 2) as,
# The outer loop run till the input 'n'
# And the inner loop runs (n - 1) times for every iteration of the outer loop.
# This program has a SC of O(n ^ 2) and I am not sure how!


class PascalsTriangleOne:

    def __init__(self):
        pass

    @staticmethod
    def print_pascals_triangle_one(upper_limit):
        pascals_triangle = []

        if upper_limit >= 1:
            pascals_triangle.append([1])
            # pascals_triangle = [[1]]

            for outer_indexer in range(1, upper_limit):
                # print("Outer indexer is: {0}.".format(outer_indexer))
                current_row = pascals_triangle[(outer_indexer - 1)]
                next_row = [1]

                for inner_indexer in range(1, len(current_row)):
                    next_row.append(current_row[(inner_indexer - 1)] + current_row[inner_indexer])
                    # print("Next row is: {0}.".format(next_row))

                next_row.append(1)
                pascals_triangle.append(next_row)
                # print("Pascals triangle is: {0}.".format(pascals_triangle))

        return pascals_triangle


ObjectPascalsTriangleOne = PascalsTriangleOne
print(ObjectPascalsTriangleOne.print_pascals_triangle_one(5))
# print(ObjectPascalsTriangleOne.print_pascals_triangle_one(0))

