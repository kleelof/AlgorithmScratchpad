import timeit, unittest, string, random
from functools import wraps


class AlgorithmEfficiencyTestingTool:

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

def aet_decorator(data_params):# don't need data_size. The data_params represent n, The scratchpad.populate() will take a multiplier
    FET = AlgorithmEfficiencyTestingTool(None)
    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            results =  FET.test_function(function, data_params)
            FET.print_test_results([results])
            return results
        return wrapper
    return inner_function

class TestDataGenerator:

    def generate(self, data_multiplier, _params=None):

        params = {
            'type': 'list',
            'fill_with': 'unsigned',
            'length': 1000,
            'sort': 'asc'
        }
        if _params:
         params.update(_params)

        if params['type'] == 'list':
            the_list = None
            if params['fill_with'] == 'str':
                pass
            else: # default is unsigned
                 the_list = self.get_list_int(range(params['length'] * data_multiplier))

            if the_list:
                if params['sort'] == 'random':
                    random.shuffle(the_list)
            return the_list

        elif params['type'] == 'str':
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(int(params['length']) * data_multiplier))

    def get_list_int(self, get_range):
        return [x for x in get_range]

    def get_list_int_random(self, get_range):
        elements = self.get_list_int(get_range)
        random.shuffle(elements)
        return elements


class DataGeneratorTests(unittest.TestCase):

    def setUp(self) -> None:
        self.generator = TestDataGenerator()

    def test_get_list_int(self):
        elements = self.generator.generate({
            'range': range(3)
        })
        self.assertEqual(elements, [0,1,2])

    def test_get_list_int_reverse(self):
        elements = self.generator.generate({
            'range': range(3,0,-1)
        })
        self.assertEqual(elements, [3,2,1])

    def test_get_str(self):
        string = self.generator.generate({
            'type': 'str',
            'length': 10
        })
        self.assertEqual(len(string), 10)

if __name__ == '__main__':
    unittest.main()