'''
    Algorithm Scratchpad is designed to assist in developing and testing algorithms.

    Below are examples of how to generate different types of test data for simple algorithms.

    Here, 'simple algorithm' just means the algorithm needs only 1 parameter. Later I will cover how to setup
    complex algorithms(those that require multiple parameters).

'''
from algorithm_efficiency_tool.tool_class import TestDataGenerator


def reverse_list(_list):
    for i in range(int(len(_list) / 2)):
        temp = _list[i]
        _list[i] = _list[len(_list) - 1 - i]
        _list[len(_list) - 1 - i] = temp


def reverse_string(string):
    letters = list(string)
    for i in range(int(len(string) / 2)):
        temp = letters[i]
        letters[i] = letters[len(letters) - 1 - i]
        letters[len(letters) - 1 - i] = temp
    return ''.join(letters)


if __name__ == '__main__':
    TDG = TestDataGenerator()

    _list = TDG.generate(1, {
        'type': 'list',
        'number_of_nodes': 5,
        'sort': 'asc'
    })
    temp = _list[::-1] # get reversed copy of list for testing against algorithm results
    reverse_list(_list)
    assert temp == _list

    _string = TDG.generate(1, {
        'type': 'str',
        'length': 1000
    })
    temp = _string[::-1]
    assert temp == reverse_string(_string)

