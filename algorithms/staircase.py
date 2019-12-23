'''
    In this algorithm, you are given a number of stairs, and a number of allowed steps.

    You have to return every combinations of the allowed steps it takes to get to the top.

    Here is a video that explains the problem and the solution: https://www.youtube.com/watch?v=NFJ3m9a1oJQ

'''
import unittest
from algorithm_efficiency_tool.tool_class import AlgorithmEfficiencyTool, aet_decorator


def top_down(steps):
    if steps <= 1:
        return 1
    return top_down(steps-1) + top_down(steps-2)


def memoize(steps, memo = None):
    if steps < 0:
        return 0
    elif steps == 0:
        return 1

    if memo is None:
        memo = [0 for i in range(steps + 1)]
        memo[0], memo[1] = 1,1

    if memo[steps] == 0:
        memo[steps] = memoize(steps - 1, memo) + memoize(steps - 2, memo)

    return memo[steps]

if __name__ == '__main__':
    top_down(1)

class StairsTests(unittest.TestCase):

    def test_top_down(self):
        self.assertEqual(13, top_down(6))
        self.assertEqual(5, top_down(4))
        self.assertEqual(1, top_down(1))
        self.assertEqual(1, top_down(0))

    def test_bottom_up(self):
        self.assertEqual(13, memoize(6))
        self.assertEqual(5, memoize(4))
        self.assertEqual(1, memoize(1))
        self.assertEqual(1, memoize(0))

    def test_compare_functions(self):
        AET = AlgorithmEfficiencyTool()

        AET.compare_algorithms([
            {
                'function': top_down,
                'data_params': {
                    'type': 'preset',
                    'fill_with': [20, 40]
                }
            },
            {
                'function': memoize,
                'data_params': {
                    'type': 'preset',
                    'fill_with': [20, 40]
                }
            }
        ])
