'''
    Animation: https://www.youtube.com/watch?v=nmhjrI-aW5o
'''
from algorithm_efficiency_tool.tool_class import aet_decorator

@aet_decorator(data_params={
    'type': 'list',
    'number_of_nodes': 10000,
    'test_run': {
        'number_of_nodes': 20000
    }
})
def bubble_sort(arr):
    for item in range(len(arr)-1,0,-1):
        for i in range(item):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

    return arr

if __name__ == '__main__':
    # assert bubble_sort([4,2,5,3,1]) == [1,2,3,4,5]

    bubble_sort([])

