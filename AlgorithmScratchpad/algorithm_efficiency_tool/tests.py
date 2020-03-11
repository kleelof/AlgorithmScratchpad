import sys
sys.path.insert(0, './')

import unittest
from AlgorithmScratchpad.algorithm_efficiency_tool.test_data_generator import TestDataGenerator


class DataGeneratorTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.generator = TestDataGenerator()

    def test_get_list_int(self):
        elements = self.generator.generate('control', {
            'number_of_nodes': 3
        })
        self.assertEqual([0,1,2], elements)

    def test_get_list_int_reverse(self):
        elements = self.generator.generate('control', {
            'number_of_nodes': 3,
            'sort': 'desc'
        })
        self.assertEqual([2,1,0], elements)

    def test_get_str(self):
        string = self.generator.generate('control', {
            'type': 'str',
            'number_of_nodes': 10
        })
        self.assertEqual(10, len(string))

    def test_get_list_of_str(self):
        number_of_nodes = 100
        length = 4
        _list = self.generator.generate('control', {
            'type': 'list',
            'fill_with': 'str',
            'length': length,
            'number_of_nodes': number_of_nodes
        })
        self.assertEqual(number_of_nodes, len(_list))
        self.assertEqual(number_of_nodes, len([x for x in _list if len(x) == length]))

    def test_get_default(self):
        self.assertEqual('I like pizza', self.generator.generate('control', {'type': 'I like pizza'}))

    def test_get_signed(self):
        number_of_nodes = 100
        _list = self.generator.generate('control', {
            'type': 'list',
            'fill_with': 'signed',
            'number_of_nodes': number_of_nodes
        })
        self.assertEqual(number_of_nodes, len(_list))
        self.assertEqual(number_of_nodes, len([x for x in _list if x < 0]))

    def test_use_control_run_data_if_have_test_run(self):
        _data_params = {
            'type': 5,
            'test_run': {
                'type': 10
            }
        }
        self.assertEqual(10, self.generator.generate('test', _data_params))

    def test_use_control_run_data_if_no_test_run(self):
        _data_params = {
            'type': 5
        }
        self.assertEqual(self.generator.generate('control', _data_params), self.generator.generate('test', _data_params))

if __name__ == '__main__':
    unittest.main()