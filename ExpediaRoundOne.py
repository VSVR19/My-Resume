class Solution:

    def __init__(self):
        pass

    @staticmethod
    def solve_every_challenge(n, p):
        counter = 0
        flag = 0
        for iterator in range(1, (n + 1)):
            if n % iterator == 0:
                print("Iterator is: {0}.".format(iterator))
                counter += 1

                if counter == p:
                    print("Counter is: {0}.".format(counter))
                    return iterator
        return 0

    def maximum_subsequence_sum(arr, threshold):
        result = 0
        indexer = 0

        while result <= threshold:
            result += arr[indexer]

            if indexer >= len(arr):
                break

        print("Result is: {0}.".format(result))


ObjectSolution = Solution
print(Solution.maximum_subsequence_sum([1,2,3,4,5,6,7,16], 15))

'''
print(Solution.solve_every_challenge(10, 3))
print(Solution.solve_every_challenge(10, 5))
print(Solution.solve_every_challenge(1, 1))
'''