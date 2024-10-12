from models.state import State
from machines.post import Post
from machines.blog import Blog


# create blog
blog = Blog(
    data={
        "id": 1,
        "posts": []
    }
)

# create posts
post_1 = Post(data={
        "blog": blog.data["id"],
        "id": 1,
        "content": "Hello, world"
})

post_2 = Post(data={
        "blog": blog.data["id"],
        "id": 2,
        "content": "Shouldn't have posted this."
})

post_3 = Post(data={
        "blog": blog.data["id"],
        "id": 3,
        "content": "I'm deleting this blog. Goodbye forever!"
})

# add posts to blog
blog.add_posts([post_1, post_2, post_3])

# manage posts
post_1.transition(State("Published"))
post_2.transition(State("Published"))
post_2.transition(State("Archived"))
post_3.transition(State("Published"))

# delete blog
blog.transition(State("Deleted"))
