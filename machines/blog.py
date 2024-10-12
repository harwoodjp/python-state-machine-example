from models.machine import Machine
from models.function import Function
from models.state import State
from models.transition import Transition
from machines.post import Post, Archived

Active = State("Active")
Inactive = State("Inactive")
Deleted = State("Deleted")


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
    data["posts"] = []


initial_state = Active
states = [Active, Inactive, Deleted]

transitions = [
    Transition(initial_state, initial_state, Function(fn=create_blog)),
    Transition(Active, Inactive, Function(fn=deactivate_blog)),
    Transition(Inactive, Active, Function(fn=activate_blog)),
    Transition(Active, Deleted, Function(fn=delete_blog)),
    Transition(Inactive, Deleted, Function(fn=delete_blog)),
]


class Blog(Machine):
    def __init__(self, data: dict):
        super().__init__(initial_state, states, transitions, data)

    def get_id(self):
        return self.data["id"]

    def add_posts(self, posts: list[Post]):
        self.data["posts"] += posts

    def get_post(self, id: int):
        for post in self.get_posts():
            if post.get_id() == id:
                return post
        return None

    def get_posts(self):
        return self.data["posts"]

    def archive_posts(self):
        for post in self.get_posts():
            if post.state.name != Archived.name:
                post.transition(Archived)
