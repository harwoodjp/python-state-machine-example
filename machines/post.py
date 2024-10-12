from models.machine import Machine
from models.state import State
from models.function import Function
from models.transition import Transition

Draft = State("Draft")
Published = State("Published")
Archived = State("Archived")


def draft_post(data):
    print(f"POST /blog/{data['blog']}/post/{data['id']}/draft")


def publish_post(data):
    print(f"POST /blog/{data['blog']}/post/{data['id']}/publish")


def archive_post(data):
    print(f"POST /blog/{data['blog']}/post/{data['id']}/archive")


initial_state = Draft
states = [Draft, Published, Archived]
transitions = [
    Transition(initial_state, initial_state, Function(fn=draft_post)),
    Transition(Draft, Published, Function(fn=publish_post)),
    Transition(Published, Archived, Function(fn=archive_post)),
]


class Post(Machine):
    def __init__(self, data: dict):
        super().__init__(initial_state, states, transitions, data)

    def get_id(self):
        return self.data["id"]
