from api.post.router import post
from api.depends import get_db
from api.models import Post
from fastapi import Depends

@post.get("/posts")
async def get_posts(db = Depends(get_db)):
    posts = Post.select()
    data =  []
    for post in posts:
        data.append([post.id, post.title, post.content, post.photo])
    return {'posts': data}