import random, string

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
                the_list = self.get_list_int(range(params['number_of_nodes'] * data_multiplier))

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