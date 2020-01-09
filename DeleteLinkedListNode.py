# This program, provided the head and the node to be deleted, deletes that node from a Linked List.
# N.B- This program does not delete head and the tail of the input linked list.
# This program was not taken from leetcode.com
# This program has a TC of O(n) as
# We might iterate through all the nodes in the linked list.
# This program has a SC of O(n) as
# We do not use any other additional data structures.


class LinkedListCreation:

    def __init__(self, value):
        self.value = value
        self.next_node = None


a = LinkedListCreation(4)
b = LinkedListCreation(5)
c = LinkedListCreation(1)
d = LinkedListCreation(9)

a.next_node = b
b.next_node = c
c.next_node = d


class DeleteLinkedListNode:

    def __init__(self):
        pass

    @staticmethod
    def print_linked_list(head_node):
        node = head_node
        while node is not None:
            print(node.value)
            node = node.next_node

    @staticmethod
    def delete_linked_list_node(head, deleted_node):
        current_node = head
        previous_node = None

        while current_node is not None:
            if current_node == deleted_node:
                previous_node.next_node = current_node.next_node
                return current_node.value

            previous_node = current_node
            current_node = current_node.next_node

    @staticmethod
    def print_check_linked_list(head):
        node = a
        while node is not None:
            print(node.value)
            node = node.next_node


ObjectDeleteLinkedListNode = DeleteLinkedListNode
# ObjectDeleteLinkedListNode.print_linked_list(a)
print(ObjectDeleteLinkedListNode.delete_linked_list_node(a, a))
ObjectDeleteLinkedListNode.print_check_linked_list(a)
