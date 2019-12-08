'''
    At the core of Algorithm Scratchpad is the AlgorithmEfficiencyTool(AET).

    One tool AET gives you is the aet_decorator.
    When the aet_decorator is applied, it generate test data to use in the algorithm

    aet_decorator:
        data_type: str | intList / strList
        data_size: number of nodes to use. ex; for a string, this will be the length of the string

    NOTE: Fully test your algorithm before applying this decorator. Once the decorator is applied, the data you used
            for development is replaced with test data
          As you use these tools, keep in mind your test data sizes. Depending on the complexity of  your algorithm,
            large data sizes can take some time. Throughout the examples and code, you will find values I have found to
            be useful for getting an accurate result within a tolerable amount of time.
'''
from AlgorithmScratchpad.algorithm_efficiency_tool import aet_decorator


@aet_decorator(data_params={
    'type': 'str',
    'length': 200000
})
def reverse_string(string):
    letters = list(string)
    for i in range(int(len(string)/2)):
        temp = letters[i]
        letters[i] = letters[len(letters) - 1 - i]
        letters[len(letters) - 1 - i] = temp
    return ''.join(letters)

@aet_decorator(data_params={
    'type': 'list',
    'length': 50
})
def move_least_to_last(_list):
    for i in range(len(_list)):
        for j in range(len(_list)):
            for k in range(len(_list)):
                for l in range(len(_list)):
                    for m in range(len(_list)):
                        pass

if __name__ == '__main__':
    # assert reverse_string('hello') == 'olleh'

    # test data is auto generated.
    #reverse_string('')

    move_least_to_last([1,2,3,4])

