'''
    How to compare functions in the same Scratchpad
'''
import unittest
from AlgorithmScratchpad.pads.single_linked_list_pad import SingleLinkedListPad


class MySingleLinkedList(SingleLinkedListPad):

    def reverse_list(self):

        if self.head is None or self.head.next is None:
            return

        node = self.head.next
        last_node = self.head
        self.head.next = None

        while node.next:
            next_node = node.next
            node.next = last_node
            last_node = node
            node = next_node
        self.head = node
        node.next = last_node

    def reverse_list_2(self):

        if self.head is None or self.head.next is None:
            return

        node = self.head

        while node.next:
            temp = self.head  # save head
            self.head = node.next
            node.next = node.next.next  # set current node next to the next of node being moved to the head
            self.head.next = temp  # set new head next to old head


class CompareFunctionsTests(unittest.TestCase):

    def setUp(self) -> None:
        self.SLL = MySingleLinkedList()

    def test_reverse_list(self):
        self.SLL.populate(1, {
            'length': 4,
            'sort': 'asc'
        })
        self.SLL.reverse_list()
        self.assertEqual(self.SLL.to_list(), [3,2,1,0])

    def test_reverse_list_2(self):
        self.SLL.populate(1, {
            'length': 4,
            'sort': 'asc'
        })
        self.SLL.reverse_list()
        self.assertEqual(self.SLL.to_list(), [3,2,1,0])

    def test_efficiency(self):
        self.SLL.data_params = {
            'length': 5000
        }
        self.SLL.test_functions([self.SLL.reverse_list, self.SLL.reverse_list_2])


if __name__ == '__main__':
    unittest.main()