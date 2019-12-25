import unittest
from scratchpad import ScratchpadBase

'''
    Use this ScratchPadBase to develop and test algorithms related to Binary Trees
    READ THE NOTES BELOW at generate_node
'''


class BinaryTreeNode(ScratchpadBase):

    def __init__(self, data = -1, _data_params = None):

        data_params = {
            'type': 'list',
            'fill_with': 'unsigned',
            'sort': 'random'
        }
        if _data_params:
            data_params.update(_data_params)

        super().__init__(data_params)

        self.data = data
        self.left = None
        self.right = None

    def append(self, node):
        if node.data < self.data:
            if self.left is None:
                self.left = node
            else:
                self.left.append(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.append(node)

    def print_me(self):
        if self.left:
            self.left.print_me()
        print(f'value: {self.data}  left: {self.left.data if self.left else "null"}  right: {self.right.data if self.right else "null"}')
        if self.right:
            self.right.print_me()

    def to_list(self, _list=None):
        if not _list:
            _list = []

        if self.left:
            self.left.to_list(_list)
        _list.append(f'value: {self.data}  left: {self.left.data if self.left else "null"}  right: {self.right.data if self.right else "null"}')
        if self.right:
            self.right.to_list(_list)
        return _list

    '''
        The following function MUST exist in any extending classes.
    '''
    def generate_node(self, value):
        return BinaryTreeNode(value) # The extending class must create an instance of itself and return it

    # this function can be overridden to create more complex test data
    def populate(self, run, _params=None):

        if _params:
            self.data_params.update(_params)

        elements = self.data_generator.generate(run, self.data_params)
        self.data = elements[0]
        self.left = None
        self.right = None

        for i in range(1, len(elements)):
            node = self.generate_node(elements[i])
            self.append(node)


class BinaryTreeTests(unittest.TestCase):

    def setUp(self) -> None:
        self.root = BinaryTreeNode(10)

    def test_populate(self):
        self.root.set_params({
            'type': 'list',
            'fill_with': 'unsigned',
            'sort': 'random',
            'number_of_nodes': 100,
            'test_run': {
                'number_of_nodes': 200
            }
        })
        self.root.populate('control')
        self.assertEqual(100, len(self.root.to_list()))
        self.root.populate('run')
        self.assertEqual(200, len(self.root.to_list()))

    def test_append_lower_value(self):
        self.root.append(self.root.generate_node(8))
        self.assertEqual(self.root.left.data, 8)

    def test_append_higher_value(self):
        self.root.append(self.root.generate_node(12))
        self.assertEqual(self.root.right.data, 12)
