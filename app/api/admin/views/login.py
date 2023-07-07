from api.admin.router import admin
from api.admin.shemas import LoginShema
from api.depends import get_db
from api.models import Admin
from fastapi import Depends

from api.depends import generate_token


@admin.post('/admin/login')
async def login(data: LoginShema, db = Depends(get_db)):
    try:
        admin = Admin.select(Admin.username==data.username and Admin.password==data.password).get()
        if admin:
            return generate_token(admin.id)
    except:
        return False
    return False