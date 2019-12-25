'''
    So far we have looked at using Algorithm Scratchpad to develop and test simple algorithms.

    You can also use Algorithm Scratchpad to create an environment for testing algorithms that require a complex data
    structure. (binary tree, single linked lists, etc....)

    Checkout the 'pads' folder for some pre-built scratchpads. NOTE: The pre-built pads are intended to be inherited to create your own scratchpad.

    In this example, I am using the SingleLinkedListPad

'''
import unittest
from pads.single_linked_list_pad import SingleLinkedListPad


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


class MySingleLinkedListTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.SLL = MySingleLinkedList({
            'number_of_nodes': 100
        })

    def setUp(self) -> None:
        self.SLL.populate('control') # rebuilds the data

    def test_reverse_list(self):
        temp = self.SLL.to_list()
        temp.reverse()
        self.SLL.reverse_list()
        self.assertEqual(temp, self.SLL.to_list())
