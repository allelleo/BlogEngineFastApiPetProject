from api.post.router import post
from fastapi import FastAPI, File, UploadFile, Depends
from api.depends import get_db
from api.depends import get_user_id_from_jwt_token
from api.models import Post

@post.delete("/post/delete")
async def create_post(post_id: int, token: str, db=Depends(get_db)):
    
    admin_id = get_user_id_from_jwt_token(token)
    if not admin_id:
        return False
    
    post = Post.get_by_id(post_id)
    if not post:
        return False
    
    post.delete()
    return True