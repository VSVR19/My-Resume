class FirstLinkedListCreation:

    def __init__(self, value):
        self.value = value
        self.next_node = None


a = FirstLinkedListCreation(4)
b = FirstLinkedListCreation(1)
c = FirstLinkedListCreation(8)
d = FirstLinkedListCreation(4)
e = FirstLinkedListCreation(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e
e.next_node = None


class SecondLinkListCreation:

    def __init__(self, value):
        self.value = value
        self.next_node = None


i = SecondLinkListCreation(5)
j = SecondLinkListCreation(0)
k = SecondLinkListCreation(1)

i.next_node = j
j.next_node = k
k.next_node = c


class LinkedListIntersection:

    def __init__(self):
        pass

    @staticmethod
    def print_first_linked_list(list_one_head, list_two_head):
        list_one_node = list_one_head
        list_two_node = list_two_head

        if list_one_node is None or list_two_node is None:
            return None

        while list_one_node != list_two_node:

            if list_one_node is None:
                list_one_node = list_two_head

            if list_two_node is None:
                list_two_node = list_one_head

            if list_one_node == list_two_node:
                return list_one_node.value

            list_one_node = list_one_node.next_node
            list_two_node = list_two_node.next_node

        return list_one_node.value


ObjectLinkedListIntersection = LinkedListIntersection()
print(ObjectLinkedListIntersection.print_first_linked_list(a, i))
