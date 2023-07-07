from fastapi import FastAPI

from .models import Admin, Post
from .db import db

db.connect()
db.create_tables(
    [
        Admin,
        Post
    ]
)
db.close()

app = FastAPI()

from .post.router import post
from .admin.router import admin

app.add_api_route(post)
app.add_api_route(admin)