from models.machine import Machine
from models.state import State
from models.function import Function
from models.transition import Transition


def draft_post(data):
    print(f"POST /blog/{data['blog']}/post/{data['id']}/draft")

def publish_post(data):
    print(f"POST /blog/{data['blog']}/post/{data['id']}/publish")

def archive_post(data):
    print(f"POST /blog/{data['blog']}/post/{data['id']}/archive")

draft_post_fn = Function(fn=draft_post)
publish_post_fn = Function(fn=publish_post)
archive_post_fn = Function(fn=archive_post)

initial_state = State("Draft")
states = [State("Draft"), State("Published"), State("Archived")]
transitions = [
    Transition(initial_state, initial_state, draft_post_fn),
    Transition(State("Draft"), State("Published"), publish_post_fn),
    Transition(State("Published"), State("Archived"), archive_post_fn),
]

class Post(Machine):
    def __init__(self, data: dict):
        super().__init__(initial_state, states, transitions, data)