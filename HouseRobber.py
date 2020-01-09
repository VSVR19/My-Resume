# https://leetcode.com/problems/house-robber/
# https://www.youtube.com/watch?v=xlvhyfcoQa4

# This program calculates the maximum bounty that can be obtained from robbing houses in a particular fashion.
# This program has a TC of O(n) as,
# We iterate through all the elements in the input array.
# This program has a SC of O(1) as,
# We are not using any significant additional memory.


class HouseRobber:

    def __init__(self):
        pass

    @staticmethod
    def determine_maximum_bounty(bounties_in_houses):
        length_bounties_in_houses = len(bounties_in_houses)
        temporary_bounties = [None] * length_bounties_in_houses
        maximum_bounty = 0

        if length_bounties_in_houses <= 0:
            maximum_bounty = 0
        elif length_bounties_in_houses == 1:
            maximum_bounty = bounties_in_houses[1]
        elif length_bounties_in_houses == 2:
            maximum_bounty = max(bounties_in_houses[0], bounties_in_houses[1])
        else:
            temporary_bounties[0] = bounties_in_houses[0]
            temporary_bounties[1] = max(bounties_in_houses[0], bounties_in_houses[1])

            for indexer in range(2, len(temporary_bounties)):
                temporary_bounties[indexer] = max((bounties_in_houses[indexer] + temporary_bounties[indexer - 2])
                                                  , temporary_bounties[(indexer - 1)])

            maximum_bounty = temporary_bounties[-1]

        return maximum_bounty


ObjectHouseRobber = HouseRobber
# print(ObjectHouseRobber.determine_maximum_bounty([1, 2, 3, 1]))
# print(ObjectHouseRobber.determine_maximum_bounty([2, 7, 9, 3, 1]))
print(ObjectHouseRobber.determine_maximum_bounty([2, 1, 1, 2]))
