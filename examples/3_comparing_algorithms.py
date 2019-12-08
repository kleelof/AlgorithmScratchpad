'''
    So far, we've seen how you can create test data for your algorithms as well as test efficiency using the aet_decorator.

    In this example, we will see how to compare 2 or more algorithms.

    This feature is the primary reason I built Algorithm Scratchpad. I often found myself wondering if my algorithm or
    one suggested by an instructor or website was the faster or more efficient algorithm.

'''
from algorithm_efficiency_tool.tool_class import AlgorithmEfficiencyTool

def reverse_string(string):
    letters = list(string)
    for i in range(int(len(string) / 2)):
        temp = letters[i]
        letters[i] = letters[len(letters) - 1 - i]
        letters[len(letters) - 1 - i] = temp
    return ''.join(letters)


def reverse_list(_list):
    for i in range(int(len(_list) / 2)):
        temp = _list[i]
        _list[i] = _list[len(_list) - 1 - i]
        _list[len(_list) - 1 - i] = temp
    return _list


if __name__ == '__main__':
    number_of_nodes = 2000000
    AET = AlgorithmEfficiencyTool()
    AET.compare_functions([
        {
            'function': reverse_string,
            'data_params': {
                                'type': 'str',
                                'number_of_nodes': number_of_nodes # in the case of strings, this will be the length of the string
                            }
        },
        {
            'function': reverse_list,
            'data_params': {
                'type': 'list',
                'number_of_nodes': number_of_nodes # In the case of lists, this is the number of elements
            }
        }
    ])