class ColorTerminalOutput:
    """Class for colored output to terminal"""

    def __init__(self):
        self.ok = '\033[92m'
        self.error = '\033[91m'
        self.ko = '\033[93m'
        self.end = '\033[0m'
        self.clear = '\033[0m'

