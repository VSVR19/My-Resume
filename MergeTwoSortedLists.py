# This program merges two sorted linked lists while maintaining the 'sorted' order.
# This program has a TC of O(m + n) which is simply O(n) as
# We traverse through all the elements in both the linked lists,
# This program has a SC of O(1) as
# We are simply 're-wiring' the existing pointers present in the two input linked lists.

# https://leetcode.com/problems/merge-two-sorted-lists/
# https://www.youtube.com/watch?v=K63Mjf-H0B0
# https://www.youtube.com/watch?v=r3MAkVZkD0s


class FirstLinkedListCreation:

    def __init__(self, value):
        self.value = value
        self.next_node = None


a = FirstLinkedListCreation(1)
b = FirstLinkedListCreation(2)
c = FirstLinkedListCreation(4)

a.next_node = b
b.next_node = c


class SecondLinkedListCreation:

    def __init__(self, value):
        self.value = value
        self.next_node = None


i = SecondLinkedListCreation(1)
j = SecondLinkedListCreation(3)
k = SecondLinkedListCreation(4)


i.next_node = j
j.next_node = k


class MergeTwoSortedLists:

    def __init__(self):
        pass

    @staticmethod
    def print_first_linked_list():
        node = a

        while node is not None:
            print(node.value)
            node = node.next_node

    @staticmethod
    def print_second_linked_list():
        node = i

        while node is not None:
            print(node.value)
            node = node.next_node

    @staticmethod
    def merge_two_sorted_lists(list_one_node, list_two_node):
        dummy = FirstLinkedListCreation(-1)
        head = dummy

        while list_one_node is not None and list_two_node is not None:
            if list_one_node.value < list_two_node.value:
                dummy.next_node = list_one_node
                list_one_node = list_one_node.next_node
            else:
                dummy.next_node = list_two_node
                list_two_node = list_two_node.next_node

            dummy = dummy.next_node

            if list_one_node is not None:
                dummy.next_node = list_one_node
            else:
                dummy.next_node = list_two_node

        return head.next_node

    @staticmethod
    def verify_merged_lists(node):
        while node is not None:
            print(node.value)
            node = node.next_node


ObjectMergeTwoSortedLists = MergeTwoSortedLists
# ObjectMergeTwoSortedLists.print_first_linked_list()
# ObjectMergeTwoSortedLists.print_second_linked_list()

ObjectMergeTwoSortedLists = MergeTwoSortedLists
head_node = ObjectMergeTwoSortedLists.merge_two_sorted_lists(a, i)
ObjectMergeTwoSortedLists.verify_merged_lists(head_node)
