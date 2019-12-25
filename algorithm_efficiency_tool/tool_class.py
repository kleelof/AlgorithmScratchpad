import timeit
from functools import wraps
from algorithm_efficiency_tool.test_data_generator import TestDataGenerator


class AlgorithmEfficiencyTool:

    def __init__(self, scratchpad=None):
        self.scratchpad = scratchpad
        self.data_generator = TestDataGenerator()

    def test_algorithm(self, function, data_params=None, print_results=False):

        results = {
            'test_name': function.__name__  if not self.scratchpad else f"{self.scratchpad.__class__.__name__}.{function.__name__}"
        }
        print(f'Testing {results["test_name"]}')

        results['run_1'] = self._run_test('control', function, data_params)
        results['run_2'] = self._run_test('test', function, data_params)

        results['multiplier'] = round(results['run_2'] / results['run_1'])
        results['o_time'] = 'O(n)' if results['multiplier'] < 3 else f'O(n{round(int(results["multiplier"]) / 2)})'

        if print_results:
            self.print_test_results(results)
        return results

    '''
        
    '''
    def _run_test(self, run, function, data_params = None):
        print(f'Run {run}: ')

        print('Populating...')
        if data_params:
            if type(data_params) is dict:
                data = self.data_generator.generate(run, data_params)
            else:
                data = [self.data_generator.generate(run, _params) for _params in data_params] # handle multiple params

        else:
            self.scratchpad.populate(run)
            data = None

        print('Testing...')
        if data:
            start = timeit.default_timer()
            function(*data)
            end=timeit.default_timer()
        else:
            start = timeit.default_timer()
            function()
            end = timeit.default_timer()

        return (end - start) * 1000

    def compare_algorithms(self, algorithms):
        results = []
        for algorithm in algorithms:
            data_params = None
            if type(algorithm) == dict:
                data_params = algorithm['data_params']
                if type(data_params) is dict:
                    data_params = [data_params]
                algorithm = algorithm['function']
            results.append(self.test_algorithm(algorithm, data_params))
        self.print_test_results(results)
        return results

    def print_test_results(self, results):
        print('\n---------------------------------------------------------------------------------------------\nResults:\n')
        print(f"| {'algorithm'.ljust(50)} | {f'Run 1: '.ljust(40)} | {f'Run 2: '.ljust(40)} | {'o_time'.ljust(15)} |")
        if type(results) is dict:
            self.print_test_results_line(results)
        else:
            for result in results:
                self.print_test_results_line(result)
        print('\n---------------------------------------------------------------------------------------------End test')

    def print_test_results_line(self, result):
        print(
            f"| {result['test_name'].ljust(50)} | {str(result['run_1']).ljust(40)} | {str(result['run_2']).ljust(40)} | {result['o_time'].ljust(15)} |")


def aet_decorator(data_params, _settings=None):# don't need data_size. The data_params represent n, The scratchpad.populate() will take a multiplier
    aet = AlgorithmEfficiencyTool(None)
    settings = {
        'return_results': True
    }
    if _settings:
        settings.update(_settings)

    if type(data_params) is dict:
        data_params = [data_params]

    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            results =  aet.test_algorithm(function, data_params)
            aet.print_test_results([results])
            return results
        return wrapper
    return inner_function