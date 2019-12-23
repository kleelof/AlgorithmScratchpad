from algorithm_efficiency_tool.tool_class import AlgorithmEfficiencyTool, TestDataGenerator


class ScratchpadBase:

    def __init__(self, data_params=None):
        self.data_generator = TestDataGenerator()
        self.data_params = data_params if data_params else {}

    def populate(self, data_multiplier=1, data_params=None):
        raise NotImplementedError()

    def compare_functions(self, functions):
        return AlgorithmEfficiencyTool(self).compare_algorithms(functions)

    def set_params(self, _params):
        self.data_params.update(_params)