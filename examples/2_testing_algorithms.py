'''
    At the core of Algorithm Scratchpad is the AlgorithmEfficiencyTool(AET). Using AET and it's available decorator,
    aet_decorator, you can easily test any algorithm or compare 2 or more algorithms.

    One tool AET gives you is the aet_decorator.
    When the aet_decorator is applied, it generates test data to use in your algorithm

    aet_decorator:
        data_params: For a full list of available settings for 'data_params' checkout the test_data_generator.py file

    NOTE: Fully test your algorithm before applying this decorator. Once the decorator is applied, the data you used
            for development is replaced with test data

          As you use these tools, keep in mind your test data sizes. Depending on the complexity of  your algorithm,
            large data sizes can take some time. Throughout the examples and code, you will see values I have found to
            be useful for getting an accurate result within a tolerable amount of time.

'''
from algorithm_efficiency_tool.tool_class import AlgorithmEfficiencyTool
from algorithm_efficiency_tool.aet_decorator import aet_decorator


@aet_decorator(data_params={
    'type': 'str',
    'number_of_nodes': 2000000
})
def reverse_string(string):
    letters = list(string)
    for i in range(int(len(string) / 2)):
        temp = letters[i]
        letters[i] = letters[len(letters) - 1 - i]
        letters[len(letters) - 1 - i] = temp
    return ''.join(letters)


@aet_decorator(data_params={
    'type': 'list',
    'number_of_nodes': 100000
})
def reverse_list(_list):
    for i in range(int(len(_list) / 2)):
        temp = _list[i]
        _list[i] = _list[len(_list) - 1 - i]
        _list[len(_list) - 1 - i] = temp
    return _list


if __name__ == '__main__':
    # both of these algorithms were tested in part one, so  we will skip testing for this.

    reverse_string('')  # the parameter for the algorithm can be anything. It will be replaced by the aet_decorator
    reverse_list([])    # when the algorithm is executed
'''
    When you run these tests, you will see output to your terminal window that looks something like this:
    
    ---------------------------------------------------------------------------------------------
    Results:
    
    | algorithm                                          | Run 1:                                   | Run 2:                                   | o_time          |
    | reverse_string                                     | 27.241544000389695                       | 54.27765399963391                        | O(n)            |
    
    ---------------------------------------------------------------------------------------------End test
    
    algorithm: The name of the algorithm. Will include the scratchpad name as well when using a scratchpad
    Run 1: The time, in milliseconds, the algorithm took to run with the control data.
    Run 2: The timme the algorithm took after doubling the control data.
    o_time: The O-notation for the algorithm.
'''
