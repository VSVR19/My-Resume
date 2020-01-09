# https://leetcode.com/problems/linked-list-cycle/solution/


class LinkedListCreation:

    def __init__(self, val):
        self.val = val
        self.next = None


a = LinkedListCreation(1)
b = LinkedListCreation(2)
# c = LinkedListCreation(0)
# d = LinkedListCreation(4)

a.next = b
# b.next = c
# c.next = d
# d.next = b

# print(a.val)
# print(a.next.val)
# print(b.next.val)
# print(c.next.val)
# print(d.next.val)


class LinkedListCycleChecker:

    @staticmethod
    def cycle_checker(head):

        if head is None or head.next is None:
            return False

        slow_pointer = head
        fast_pointer = head.next

        while fast_pointer is not None or fast_pointer.next is not None:

            if slow_pointer == fast_pointer:
                return True

            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return False


ObjectLinkedListCycleChecker = LinkedListCycleChecker
print(ObjectLinkedListCycleChecker.cycle_checker(a))
