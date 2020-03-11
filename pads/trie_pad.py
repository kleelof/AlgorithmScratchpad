from scratchpad import ScratchpadBase
from string import ascii_lowercase

class TriePad(ScratchpadBase):
    def __init__(self):
        self.root_node = None

class TrieNode:
    def __init__(self):
        self.is_complete = False
        self.children = dict()
        for l in ascii_lowercase:
            self.children[l] = None
        