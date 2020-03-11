import sys
sys.path.insert(0, './')

import unittest
from examples.E_comparing_algorithms_II import MySingleLinkedList

class MySingleLinkedListTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.SLL = MySingleLinkedList({
            'number_of_nodes': 200,
            'test_run': {
                'number_of_nodes': 400
            }
        })

    def setUp(self) -> None:
        self.SLL.populate('control')  # rebuilds the data

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
        self.SLL.compare_algorithms([
                                    self.SLL.reverse_list,
                                    self.SLL.reverse_list_2
                                   ])  # NOTICE: The function names do not have the parenthesis. Just the function name