from pydantic import BaseModel


class Friend(BaseModel):
    id: int
    user_id: int
    friend_id: int
