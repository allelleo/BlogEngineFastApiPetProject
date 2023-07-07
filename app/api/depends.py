from .db import db
from fastapi import Depends

import jwt
import datetime


async def reset_db_state():
    db._state._state.set(db.db_state_default.copy())
    db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        db.connect()
        print(f"Connect to database successfully")
        yield
    finally:
        if not db.is_closed():
            db.close()


token = "SECRET"


def generate_token(user_id: int) -> str:
    payload = {
        "id": user_id,
        "exp": datetime.datetime.utcnow()
        + datetime.timedelta(minutes=60 * 60 * 24 * 30),
        "iat": datetime.datetime.utcnow(),
    }

    token = jwt.encode(payload=payload, key=token, algorithm="HS256")

    return token


def get_user_id_from_jwt_token(token: str) -> int:
    try:
        payload = jwt.decode(token, key=token, algorithms=["HS256"])
    except:
        return False

    user_id = payload.get("id", None)

    if user_id:
        if isinstance(user_id, int):
            return user_id

    return False
