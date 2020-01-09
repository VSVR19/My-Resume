# https://leetcode.com/problems/reverse-linked-list/


# This program reverses a linked list.
# This program has a TC of O(n)
# And a SC of O(1).
class LinkedListCreation:

    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_linked_list(head):
    # Constant memory operations.
    # SC of O(1).
    current = head
    previous = None
    next_node = None

    # Traverse till the last node.
    # We will traverse all the nodes in the linked list.
    # So we have a TC of O(n).
    while current:
        # All the 4 steps utilize constant memory.

        # Make a copy of the next node.
        next_node = current.next
        # The next node of the current node in question is set as the previous node.
        current.next = previous

        # Get ready for the next iteration.
        # The current node in question becomes the previous node.
        previous = current
        # The next_node, created in Step 1, becomes the current node for the next iteration.
        current = next_node

    print("Previous is: {0}.".format(previous.val))

    # Why previous becomes the 'new head'?
    # Not current or next_node?
    # Because, both current and next_node can be the 'None' node due to Steps 1 and 4.
    head = previous

    return head


a = LinkedListCreation(1)
b = LinkedListCreation(2)
c = LinkedListCreation(3)
d = LinkedListCreation(4)

a.next = b
b.next = c
c.next = d

print("*****BEFORE REVERSAL*****")
print(a.next.val)
print(b.next.val)
print(c.next.val)

reverse_linked_list(a)

print("*****AFTER REVERSAL*****")
print(b.next.val)
print(c.next.val)
print(d.next.val)
