from models.machine import Machine
from models.function import Function
from models.state import State
from models.transition import Transition


def create_blog(data):
    print(f"POST /blog/{data['id']}")

def activate_blog(data):
    print(f"POST /blog/{data['id']}/activate")

def deactivate_blog(data):
    print(f"POST /blog/{data['id']}/deactivate")

def delete_blog(data):
    for post in data["posts"]:
        print(f"DELETE /api/blog/{data['id']}/post/{post.data['id']}")
    print(f"DELETE /api/blog/{data['id']}")

create_blog_fn = Function(fn=create_blog)
activate_blog_fn = Function(fn=activate_blog)
deactivate_blog_fn = Function(fn=deactivate_blog)
delete_blog_fn = Function(fn=delete_blog)

initial_state = State("Active")
states = [State("Active"), State("Inactive"), State("Deleted")]

transitions = [
    Transition(initial_state, initial_state, create_blog_fn),
    Transition(State("Active"), State("Inactive"), deactivate_blog_fn),
    Transition(State("Inactive"), State("Active"), activate_blog_fn),
    Transition(State("Active"), State("Deleted"), delete_blog_fn),
    Transition(State("Inactive"), State("Deleted"), delete_blog_fn),
]

class Blog(Machine):
    def __init__(self, data: dict):
        super().__init__(initial_state, states, transitions, data)
    def add_posts(self, posts: list):
        self.data["posts"] += posts