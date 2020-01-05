'''
    Animation: https://www.youtube.com/watch?v=xWBP4lzkoyM
'''
from algorithm_efficiency_tool.tool_class import aet_decorator

@aet_decorator(data_params={
    'type': 'list',
    'number_of_nodes': 10000,
    'test_run': {
        'number_of_nodes': 20000
    }
})
def selection_sort(arr):
    for i in range(len(arr)):
        lowest_value = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest_value]:
                lowest_value_index = j
        arr[i], arr[lowest_value] = arr[lowest_value], arr[i]
    return arr


if __name__ == '__main__':
    # assert selection_sort([4,1,3,5,2]) == [1,2,3,4,5]

    selection_sort([])