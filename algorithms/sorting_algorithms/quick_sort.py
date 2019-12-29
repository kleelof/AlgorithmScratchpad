from algorithm_efficiency_tool.tool_class import aet_decorator


@aet_decorator(data_params={
    'type': 'list',
    'number_of_nodes': 1000000,
    'test_run': {
        'number_of_nodes': 2000000
    }
})
def quick_sort(arr):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(arr, 0, len(arr) - 1)
    return arr


def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    # assert quick_sort([5,3,2,4,1]) == [1,2,3,4,5]

    quick_sort([])





