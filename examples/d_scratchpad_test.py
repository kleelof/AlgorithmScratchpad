import sys
sys.path.insert(0, './')

import unittest
from examples.D_scratchpad import MySingleLinkedList

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