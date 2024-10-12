from models.state import State
from models.transition import Transition


class Machine:
    def __init__(
        self,
        initial_state: State,
        states: list[State],
        transitions: list[Transition],
        data: dict,
    ):
        self.state = initial_state
        self.states = states
        self.transitions = transitions
        self.data = data
        self.transition(self.state)

    def transition(self, to_state: State):
        for transition in self.transitions:
            _from_state = transition.from_state.name == self.state.name
            _to_state = transition.to_state.name == to_state.name
            if _from_state and _to_state:
                transition.function(self.data)
                self.state = to_state
                return
        raise ValueError(
            "Invalid transition",
            {
                "from_state": self.state.name,
                "to_state": to_state.name,
            },
        )
