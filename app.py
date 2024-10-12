from models.state import State
from machines.post import Post
from machines.blog import Blog


# create blog
blog = Blog({
        "id": 1,
        "posts": []
    }
)

# assert state
assert blog.state.name == "Active"

# add posts to blog
blog.add_posts([
    Post({
            "blog": blog.data["id"],
            "id": 1,
            "content": "Hello, world"
    }),
    Post({
            "blog": blog.data["id"],
            "id": 2,
            "content": "Shouldn't have posted this."
    }),
    Post({
            "blog": blog.data["id"],
            "id": 3,
            "content": "I'm deleting this blog. Goodbye forever!"
    })    
])

# manage posts
blog.get_post(1).transition(State("Published"))
blog.get_post(2).transition(State("Published"))
blog.get_post(2).transition(State("Archived"))
blog.get_post(3).transition(State("Published"))

# archive posts
blog.archive_posts()

# assert state and effects 
assert all(post.state.name == "Archived" for post in blog.data["posts"])

# delete blog
blog.transition(State("Deleted"))

# assert state and effects
assert blog.state.name == "Deleted"
assert blog.data["id"] == None
assert len(blog.data["posts"]) == 0