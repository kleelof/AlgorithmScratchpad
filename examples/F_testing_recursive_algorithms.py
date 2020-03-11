'''
    This example demonstrates how to preset the data you want to use for each individual run.
'''
from algorithm_efficiency_tool.tool_class import aet_decorator, AlgorithmEfficiencyTool

''' Technique 1. Build a 'starter' function that uses the AET decorator '''
@aet_decorator({
                    'type': 100,
                    'test_run': {
                        'type': 200
                    }
                })
def start_staircase_algorithm(steps):
    return staircase_algorithm(steps)


def staircase_algorithm(steps, memo = None):
    if steps < 0:
        return 0
    elif steps == 0:
        return 1

    if memo is None:
        memo = [0 for i in range(steps + 1)]
        memo[0], memo[1] = 1,1

    if memo[steps] == 0:
        memo[steps] = staircase_algorithm(steps - 1, memo) + staircase_algorithm(steps - 2, memo)

    return memo[steps]


if __name__ == '__main__':
    ''' Call the trigger function for technique 1 '''
    start_staircase_algorithm(10) # it does not matter what value you put here. AET will replace it with test data.

    ''' technique 2, use the AET directly '''
    AlgorithmEfficiencyTool().test_algorithm(staircase_algorithm,
                       [{
                            'type': 200,
                            'test_run': {
                                'type': 400
                            }
                        }],
                       True
                       )