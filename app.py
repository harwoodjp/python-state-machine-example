from machines.post import Post
from machines.blog import Blog
from machines.post import Published, Archived, Draft
from machines.blog import Active, Deleted

# create blog
blog = Blog({"id": 1, "posts": []})

# assert state
assert blog.state == Active

# add posts
blog.add_posts(
    [
        Post({"blog": blog.get_id(), "id": 1, "content": "Hello, world"}),
        Post(
            {"blog": blog.get_id(), "id": 2, "content": "Shouldn't have posted this."}
        ),
        Post(
            {
                "blog": blog.get_id(),
                "id": 3,
                "content": "I'm deleting this blog. Goodbye forever!",
            }
        ),
    ]
)

# assert state
assert all(post.state == Draft for post in blog.get_posts())

# transition posts
blog.get_post(1).transition(Published)
blog.get_post(2).transition(Published)
blog.get_post(2).transition(Archived)
blog.get_post(3).transition(Published)

# archive posts
blog.archive_posts()

# assert state
assert all(post.state == Archived for post in blog.get_posts())

# delete blog
blog.transition(Deleted)

# assert state and effects
assert blog.state == Deleted
assert len(blog.get_posts()) == 0
try:
    blog.transition(Active)
    assert False
except ValueError:
    pass
