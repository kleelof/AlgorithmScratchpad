import unittest
from algorithm_efficiency_tool.test_data_generator import TestDataGenerator


class DataGeneratorTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.generator = TestDataGenerator()

    def test_get_list_int(self):
        elements = self.generator.generate({
            'number_of_nodes': 3
        })
        self.assertEqual([0,1,2], elements)

    def test_get_list_int_reverse(self):
        elements = self.generator.generate({
            'number_of_nodes': 3,
            'sort': 'desc'
        })
        self.assertEqual([2,1,0], elements)

    def test_get_str(self):
        string = self.generator.generate({
            'type': 'str',
            'number_of_nodes': 10
        })
        self.assertEqual(10, len(string))

    def test_get_list_of_str(self):
        number_of_nodes = 100
        length = 4
        _list = self.generator.generate({
            'type': 'list',
            'fill_with': 'str',
            'length': length,
            'number_of_nodes': number_of_nodes
        })
        self.assertEqual(number_of_nodes, len(_list))
        self.assertEqual(number_of_nodes, len([x for x in _list if len(x) == length]))

    def test_get_default(self):
        self.assertEqual('I like pizza', self.generator.generate({'type': 'I like pizza'}))

    def test_get_signed(self):
        number_of_nodes = 100
        _list = self.generator.generate({
            'type': 'list',
            'fill_with': 'signed',
            'number_of_nodes': number_of_nodes
        })
        self.assertEqual(number_of_nodes, len(_list))
        self.assertEqual(number_of_nodes, len([x for x in _list if x < 0]))

if __name__ == '__main__':
    unittest.main()