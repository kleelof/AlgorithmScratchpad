import random, string
import exrex

class TestDataGenerator:

    def generate(self, data_multiplier, _params=None):

        params = {
            'type': 'list',
            'fill_with': 'unsigned',
            'number_of_nodes': 1000,
            'sort': '',
            'length': 10,
            'regex': '[a-z][A-Z][0-9]'
        }
        if _params:
            params.update(_params)
        number_of_nodes = params['number_of_nodes']

        if params['type'] == 'list':
            the_list = None
            if params['fill_with'] == 'str':
                the_list = [self.get_random_string(params['length'], params['regex']) for x in range(number_of_nodes * data_multiplier)]
            elif params['fill_with'] == 'signed':
                the_list = [x for x in range(-1, -(number_of_nodes * data_multiplier + 1), -1)]
            else: # default is unsigned
                the_list = [x for x in range(number_of_nodes * data_multiplier)]

            if the_list:
                if params['sort'] == 'random':
                    random.shuffle(the_list)
                elif params['sort'] == 'desc':
                    the_list.sort(reverse=True)
                elif params['sort'] == 'asc':
                    the_list.sort()
            return the_list

        elif params['type'] == 'str':
            return self.get_random_string(number_of_nodes * data_multiplier, params['regex'])

        else: # default is the value of type is returned. This lets the tester send a set value to be used instead.
            return params['type']

    def get_random_string(self, number_of_nodes, regex):
        letters = exrex.getone(regex)
        return ''.join(random.choice(exrex.getone(regex)) for i in range(number_of_nodes))
