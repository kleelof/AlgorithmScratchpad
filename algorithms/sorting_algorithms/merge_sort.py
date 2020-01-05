'''
   Video explanation: https://www.youtube.com/watch?v=JSceec-wEyw
'''
from algorithm_efficiency_tool.tool_class import AlgorithmEfficiencyTool

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list




if __name__ == '__main__':
    #assert merge_sort([5,3,2,4,1]) == [1,2,3,4,5]

    AlgorithmEfficiencyTool().test_algorithm(
        merge_sort,
        [{
            'type': 'list',
            'number_of_nodes': 1000000,
            'test_run': {
                'number_of_nodes': 2000000
            }
        }],
        True
    )



