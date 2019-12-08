import timeit
from algorithm_efficiency_tool.test_data_generator import TestDataGenerator


class AlgorithmEfficiencyTool:

    def __init__(self, scratchpad=None):
        self.scratchpad = scratchpad
        self.data_generator = TestDataGenerator()

    def test_function(self, function, data_params=None ):

        test_name = function.__name__
        if self.scratchpad:
            test_name = f"{self.scratchpad.__class__.__name__}.{function.__name__}"

        results = {'test_name': test_name}
        print(f'Testing: {test_name}')
        print(f'Run 1:')

        print('Populating...')
        if self.scratchpad:
            self.scratchpad.populate(1)
            data = None
        else:
             data = self.data_generator.generate(1, data_params)

        print('Testing...')
        results['run_1'] = self._run_time_iteration(function, data)

        print(f'Run 2:')
        print('Populating...')
        if self.scratchpad:
            self.scratchpad.populate(2)
            data = None
        else:
            data = self.data_generator.generate(2, data_params)

        print('Testing...')
        results['run_2'] = self._run_time_iteration(function, data)
        results['multiplier'] = round(results['run_2'] / results['run_1'])

        if results['multiplier'] < 3:
            o_time = 'n'
        else:
            o_time = f'n{round(int(results["multiplier"]) / 2)}'
        results['o_time'] = f'O({o_time})'

        return results

    def test_functions(self, functions):
        results = []
        for function in functions:
            results.append(self.test_function(function))
        self.print_test_results(results)
        return results

    def print_test_results(self, results):
        print('\n---------------------------------------------------------------------------------------------\nResults:\n')
        print(f"| {'function'.ljust(50)} | {f'Run 1: '.ljust(40)} | {f'Run 2: '.ljust(40)} | {'o_time'.ljust(15)} |")
        for result in results:
            print(f"| {result['test_name'].ljust(50)} | {str(result['run_1']).ljust(40)} | {str(result['run_2']).ljust(40)} | {result['o_time'].ljust(15)} |")

    def _run_time_iteration(self, function, data=None):
        if data:
            start = timeit.default_timer()
            function(data)
            end=timeit.default_timer()
        else:
            start = timeit.default_timer()
            function()
            end = timeit.default_timer()
        return (end - start) * 1000