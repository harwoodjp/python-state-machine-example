from models.state import State

class Transition:
    def __init__(self, from_state: State, to_state: State, function: callable):
        self.from_state = from_state
        self.to_state = to_state
        self.function = function
