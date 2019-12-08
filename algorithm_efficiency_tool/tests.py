import unittest
from algorithm_efficiency_tool.test_data_generator import TestDataGenerator

class DataGeneratorTests(unittest.TestCase):

    def setUp(self) -> None:
        self.generator = TestDataGenerator()

    def test_get_list_int(self):
        elements = self.generator.generate({
            'range': range(3)
        })
        self.assertEqual(elements, [0,1,2])

    def test_get_list_int_reverse(self):
        elements = self.generator.generate({
            'range': range(3,0,-1)
        })
        self.assertEqual(elements, [3,2,1])

    def test_get_str(self):
        string = self.generator.generate({
            'type': 'str',
            'length': 10
        })
        self.assertEqual(len(string), 10)

if __name__ == '__main__':
    unittest.main()