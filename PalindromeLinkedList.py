# https://leetcode.com/problems/palindrome-linked-list/submissions/

# This program determines if a linked list is a palindrome or not.
# This program has a TC of O(n)
# And a SC of O(1).


class LinkedListCreation:

    def __init__(self, val):
        self.val = val
        self.next = None


a = LinkedListCreation(1)
b = LinkedListCreation(2)
c = LinkedListCreation(2)
d = LinkedListCreation(1)
# e = LinkedListCreation(5)
# f = LinkedListCreation('A')
# g = LinkedListCreation('L')
# h = LinkedListCreation('A')
# i = LinkedListCreation('M')

a.next = b
b.next = c
c.next = d
# d.next_node = e
# d.next_node = e
# e.next_node = f
# f.next_node = g
# g.next_node = h
# h.next_node = i


class PalindromeLinkedList:

    @staticmethod
    def traverse_linked_list(head):
        # Allocate two pointers.
        # Constant memory operations.
        slow_marker = head
        fast_marker = head

        # This While loop via slow_marker, determines the midpoint of the linked list.
        # Excluding 'Null',
        # For a linked list with odd number of elements, fast_pointer will land at the final node
        # and for a linked list with even number of element, fast_pointer will land at 'null'.

        # We will be traversing all the elements of the linked list.
        # So we have a TC of O(n).
        while fast_marker is not None and fast_marker.next is not None:

            # Constant memory operations.
            slow_marker = slow_marker.next
            fast_marker = fast_marker.next.next

        # Now that we have determined the midpoint of the linked list,
        # the fast_marker can be reset to the head of the linked list.
        fast_marker = head
        # The second half of the linked list will be reversed.
        # This slow_marker is the head of the reversed linked list.

        # Reversing a linked list costs O(n) TC.
        slow_marker = reverse_linked_list(slow_marker)

        # Compare:
        # The un-reversed first half of the linked list
        # with the second half of reversed linked list.

        # Comparing both the linked lists is same as traversing all the elements in the input linked lists.
        # So we have a TC of O(n).
        while slow_marker:
            print(slow_marker.val)
            print(fast_marker.val)

            # If the linked list is a palindrome, all the nodes will be same.
            # If not, the linked list is not a palindrome; break- exit the loop.
            if slow_marker.val != fast_marker.val:
                return False

            # Move the slow and fast_markers for every iteration.
            slow_marker = slow_marker.next
            fast_marker = fast_marker.next

        return True


# This method reverses the second half of the linked list.
def reverse_linked_list(head):
    # Allocate variables.
    current = head
    next_node = None
    previous_node = None

    # Loop till the last element in the linked list.
    while current:
        # Make a copy of the next node.
        next_node = current.next
        # Overwrite the current nodes' next node.
        current.next = previous_node

        # Get ready for the next iteration.
        # The node being used now becomes the previous node.
        previous_node = current
        # The node created in Step 1 becomes the next node.
        current = next_node

    # The previous_node becomes the 'new head.'
    head = previous_node
    return head


ObjectPalindromeLinkedList = PalindromeLinkedList
print(ObjectPalindromeLinkedList.traverse_linked_list(a))