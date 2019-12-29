from algorithm_efficiency_tool.tool_class import aet_decorator

@aet_decorator(data_params={
    'type': 'list',
    'number_of_nodes': 10000000,
    'test_run': {
        'number_of_nodes': 20000000
    }
})
def insertion_sort(arr):
    for i in range(1, len(arr)):
        item_to_insert = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > item_to_insert:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item_to_insert
    return arr


if __name__ == '__main__':
    # assert insertion_sort([5,3,2,4,1]) == [1,2,3,4,5]

    insertion_sort([])

