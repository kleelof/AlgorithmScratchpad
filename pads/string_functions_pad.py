from AlgorithmScratchpad.scratchpad import ScratchpadBase, TestDataGenerator, sratchpad_decorator

class StringFunctionsPad(ScratchpadBase):

    def __init__(self):
        super().__init__()
        self.string = 'hello_world'

    def populate(self, data_desc=None):
        self.string = self.data_generator.generate(data_desc if data_desc else {})


