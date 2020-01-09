import collections


   # def groupAnagrams(strs):
    #     ans = collections.defaultdict(list)
    #     print("Type ")
    #
    #     for s in strs:
    #         ans[tuple(sorted(s))].append(s)
    #         print("Ans is: {0}.".format(ans))
    #
    #     return ans.values()
class Solution:
    @staticmethod
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        print("Ans: {0}.".format(ans))
        print("Type of Ans: {0}.".format(type(ans)))

        for s in strs:
            count = [0] * 26
            print("Count: {0}.".format(count))
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)

            print("Ans in loop: {0}.".format(ans))


        return ans.values()



ObjectSolution = Solution
print(ObjectSolution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


