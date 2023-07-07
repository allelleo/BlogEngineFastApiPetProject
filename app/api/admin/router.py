from fastapi import APIRouter

admin = APIRouter()

from .views.login import login