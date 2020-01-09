class Solution:

    def __init__(self):
        pass

    @staticmethod
    def uncommonFromSentences(sentence_one: str, sentence_two: str):
        result_dict = {}
        result_list = []

        sentence_one = sentence_one.split(" ")
        sentence_two = sentence_two.split(" ")

        # result_sentence = sentence_one.split(" ") + sentence_two.split(" ")

        # for word in result_sentence:
        #     if result_sentence.count(word) == 1:
        #         result_list.append(word)
        #
        # print(result_list)

        for word in sentence_one:
            if word not in result_dict:
                result_dict[word] = 1
            else:
                result_dict[word] += 1

        # print(result_dict)

        for word in sentence_two:
            if word in result_dict:
                result_dict[word] += 1
            else:
                result_dict[word] = 1

        # print(result_dict)

        for key, value in result_dict.items():
            if value == 1:
                result_list.append(key)

        print("The Uncommon word is: {0}.".format(result_list))


ObjectSolution = Solution
ObjectSolution.uncommonFromSentences("apple apple", "banana")
ObjectSolution.uncommonFromSentences("s z z z s", "s z ejt")
