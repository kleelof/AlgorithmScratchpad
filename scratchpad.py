from AlgorithmScratchpad.algorithm_efficiency_tool import AlgorithmEfficiencyTestingTool, TestDataGenerator


class ScratchpadBase:

    def __init__(self):
        self.data_generator = TestDataGenerator()
        self.data_params = {}

    def populate(self, data_multiplier, data_params=None):
        raise NotImplementedError()

    def test_functions(self, functions):
        return AlgorithmEfficiencyTestingTool(self).test_functions(functions)
