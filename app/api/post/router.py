from fastapi import APIRouter

post = APIRouter()

from .views.create import create_post
from .views.delete import delete_post
from .views.read import get_posts