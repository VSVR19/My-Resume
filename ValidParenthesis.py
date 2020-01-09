# https://leetcode.com/problems/valid-parentheses/

class ValidParenthesis:

    def __init__(self):
        pass

    @staticmethod
    def check_valid_parenthesis(input_parenthesis):
        open_parenthesis = {'(', '{', '['}
        close_parenthesis = {')', '}', ']'}
        result = True

        matching_tuples = {('(', ')'), ('{', '}'), ('[', ']')}
        holding_stack = []

        for unit_parenthesis in input_parenthesis:
            # print("Unit parenthesis is: {0}.".format(unit_parenthesis))

            if unit_parenthesis in open_parenthesis:
                holding_stack.append(unit_parenthesis)
                # print("Holding stack is: {0}.".format(holding_stack))

            elif unit_parenthesis in close_parenthesis:
                if len(holding_stack) >= 1:
                    popped_element = holding_stack.pop()
                else:
                    result = False
                    break

                if (popped_element, unit_parenthesis) not in matching_tuples:
                    result = False
                    break

        if len(holding_stack) >= 1:
            result = False

        return result


ObjectValidParenthesis = ValidParenthesis
# print(ObjectValidParenthesis.check_valid_parenthesis('()'))
# print(ObjectValidParenthesis.check_valid_parenthesis('()[]{}'))
# print(ObjectValidParenthesis.check_valid_parenthesis('{]'))
# print(ObjectValidParenthesis.check_valid_parenthesis('([)]'))
# print(ObjectValidParenthesis.check_valid_parenthesis('{[]}'))
# print(ObjectValidParenthesis.check_valid_parenthesis('['))
# print(ObjectValidParenthesis.check_valid_parenthesis(')(())'))
# print(ObjectValidParenthesis.check_valid_parenthesis(""))
# print(ObjectValidParenthesis.check_valid_parenthesis('(('))
print(ObjectValidParenthesis.check_valid_parenthesis("[])"))
