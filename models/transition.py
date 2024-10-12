from models.state import State
from models.function import Function


class Transition:
    def __init__(self, from_state: State, to_state: State, function: Function):
        self.from_state = from_state
        self.to_state = to_state
        self.function = function
