import timeit
from functools import wraps
from algorithm_efficiency_tool.test_data_generator import TestDataGenerator


class AlgorithmEfficiencyTool:

    def __init__(self, scratchpad=None):
        self.scratchpad = scratchpad
        self.data_generator = TestDataGenerator()

    #todo: add ability to choose return results or output. Then aet_decorator can overriden and sent params are allowed to pass through
    def test_function(self, function, data_params=None, return_results=True):

        test_name = function.__name__
        if self.scratchpad:
            test_name = f"{self.scratchpad.__class__.__name__}.{function.__name__}"

        results = {'test_name': test_name}
        print(f'Testing {test_name}')

        for data_multiplier in range(1, 3):
            results[f'run_{data_multiplier}'] = self._run_test(data_multiplier, function, data_params)

        results['multiplier'] = round(results['run_2'] / results['run_1'])

        if results['multiplier'] < 3:
            o_time = 'n'
        else:
            o_time = f'n{round(int(results["multiplier"]) / 2)}'
        results['o_time'] = f'O({o_time})'

        return results

    def _run_test(self, data_multiplier, function, data_params):
        print(f'Run {data_multiplier}: ')

        print('Populating...')
        if data_params:
            data = []
            for _params in data_params:
                data.append(self.data_generator.generate(data_multiplier, _params))
        else:
            self.scratchpad.populate(data_multiplier)
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

    def compare_functions(self, functions):
        results = []
        for function in functions:
            data_params = None
            if type(function) == dict:
                data_params = function['data_params']
                if type(data_params) is dict:
                    data_params = [data_params]
                function = function['function']
            results.append(self.test_function(function, data_params))
        self.print_test_results(results)
        return results

    def print_test_results(self, results):
        print('\n---------------------------------------------------------------------------------------------\nResults:\n')
        print(f"| {'algorithm'.ljust(50)} | {f'Run 1: '.ljust(40)} | {f'Run 2: '.ljust(40)} | {'o_time'.ljust(15)} |")
        for result in results:
            print(f"| {result['test_name'].ljust(50)} | {str(result['run_1']).ljust(40)} | {str(result['run_2']).ljust(40)} | {result['o_time'].ljust(15)} |")
        print('\n---------------------------------------------------------------------------------------------End test')


def aet_decorator(data_params, _settings=None):# don't need data_size. The data_params represent n, The scratchpad.populate() will take a multiplier
    FET = AlgorithmEfficiencyTool(None)
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
            results =  FET.test_function(function, data_params)
            FET.print_test_results([results])
            return results
        return wrapper
    return inner_function