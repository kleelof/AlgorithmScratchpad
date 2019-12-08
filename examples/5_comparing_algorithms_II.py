'''
    In the example Comparing Algorithms, we saw how to test 2 simple algorithms. In this example, we will look at how
    to test algorithms in the same sketchpad
'''
import unittest
from pads.single_linked_list_pad import SingleLinkedListPad


class MySingleLinkedList(SingleLinkedListPad):

    # my approach
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

    # alternate approach
    def reverse_list_2(self):
        if self.head is None or self.head.next is None:
            return
        node = self.head
        while node.next:
            temp = self.head
            self.head = node.next
            node.next = node.next.next
            self.head.next = temp

class MySingleLinkedListTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.SLL = MySingleLinkedList()

    def setUp(self) -> None:
        self.SLL.data_params = {
            'number_of_nodes': 100
        }
        self.SLL.populate()  # rebuilds the data

    def test_reverse_list(self):
        temp = self.SLL.to_list()  # get current list order
        temp.reverse()  # reverse it for the upcoming assert
        self.SLL.reverse_list()  # perform action
        self.assertEqual(temp, self.SLL.to_list())

    def test_reverse_list_2(self):
        temp = self.SLL.to_list()  # get current list order
        temp.reverse()  # reverse it for the upcoming assert
        self.SLL.reverse_list_2()  # perform action
        self.assertEqual(temp, self.SLL.to_list())

    def test_compare_algorithms(self):
        number_of_nodes = 5000
        self.SLL.populate(1, {
            'number_of_nodes': number_of_nodes
        }) # can update the data_params
        self.SLL.compare_functions([
                                    self.SLL.reverse_list,
                                    self.SLL.reverse_list_2
                                   ])  # NOTICE: The function names do not have the parenthesis. Just the function name


