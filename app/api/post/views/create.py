from api.post.router import post
from fastapi import FastAPI, File, UploadFile, Depends
from api.depends import get_db
from api.depends import get_user_id_from_jwt_token
from api.models import Post


@post.post("/post/create")
async def create_post(
    title: str, content: str, image: UploadFile, token: str, db=Depends(get_db)
):
    admin_id = get_user_id_from_jwt_token(token)
    if not admin_id:
        return False

    contents = image.file.read()
    with open(image.filename, "wb") as f:
        f.write(contents)
    p = Post(title=title, content=content, image=image.filename)
    p.save()
    
    return p.id