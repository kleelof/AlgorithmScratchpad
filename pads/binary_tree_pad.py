import unittest
from AlgorithmScratchpad.scratchpad import ScratchpadBase

'''
    Use this ScratchPadBase to develop and test algorithms related to Binary Trees
    READ THE NOTES BELOW at generate_node
'''


class BinaryTreeNode(ScratchpadBase):

    def __init__(self, data = -1, left = None, right = None):
        super().__init__()
        self.data = data
        self.left = left
        self.right = right

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
    def populate(self, data_multiplier, _params=None):
        params = {
            'type': 'list'
        }
        if _params:
            params.update(_params)
        params['range'] = range(params['length'] * data_multiplier)

        elements = self.data_generator.generate(params)
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
        self.root.populate(1, {'length': 100})
        self.assertEqual(len(self.root.to_list()), 100)
        self.root.populate(3, {'length': 100})
        self.assertEqual(len(self.root.to_list()), 300)

    def test_append_lower_value(self):
        self.root.append(self.root.generate_node(8))
        self.assertEqual(self.root.left.data, 8)

    def test_append_higher_value(self):
        self.root.append(self.root.generate_node(12))
        self.assertEqual(self.root.right.data, 12)



if __name__ == '__main__':
    unittest.main()