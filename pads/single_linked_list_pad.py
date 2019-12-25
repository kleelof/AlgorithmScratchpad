import unittest
from scratchpad import ScratchpadBase


class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

'''
    Use this class for basic functionality.
    This class is meant to be used to create an environment that you can  test Single List alorithms
'''


class SingleLinkedListPad(ScratchpadBase):

    def __init__(self, _data_params=None):

        data_params = {
            'type': 'list',
            'fill_with': 'unsigned',
            'sort': 'random'
        }
        if _data_params:
            data_params.update(_data_params)

        super().__init__(data_params)
        self.head = None


    def add_node(self, value):
        if not self.head:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def print_me(self):
        if not self.head:
            return
        node = self.head
        while node.next:
            print(f'value: {node.value}  next: {node.next}')
            node = node.next
        print(f'value: {node.value}  next: {node.next}')

    def to_list(self):
        if not self.head:
            return
        node = self.head
        _list = [node.value]
        while node.next:
            _list.append(node.next.value)
            node = node.next
        return _list

    # this function can be overridden to create more complex test data
    def populate(self, run, _params=None):

        if not _params:
            _params = self.data_params

        if _params:
            self.data_params.update(_params)
        elements = self.data_generator.generate(run, self.data_params)
        for value in elements:
            self.add_node(value)


class SingleLinkedListPadTest(unittest.TestCase):

    def setUp(self) -> None:
        self.SLL = SingleLinkedListPad({
            'type': 'list',
            'fill_with': 'unsigned',
            'sort': 'random',
            'number_of_nodes': 5,
            'test_run': {
                'number_of_nodes': 10
            }
        })

    def test_populate_control(self):
        self.SLL.populate('control')
        self.assertEqual(5, len(self.SLL.to_list()))

    def test_populate_test(self):
        self.SLL.populate('test')
        self.assertEqual(10, len(self.SLL.to_list()))