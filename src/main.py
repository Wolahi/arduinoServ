from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession


from .database import get_async_session
from .friends.modles import FriendTable
from .friends.shemas import Friend

app = FastAPI(
    title="VK TESt"
)


origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)


@app.post("/friends")
async def create_friends(friends: Friend, db: AsyncSession = Depends(get_async_session)):
    friendUser = FriendTable(user_id=friends.user_id, friend_id=friends.friend_id)
    userFriend = FriendTable(user_id=friends.friend_id, friend_id=friends.user_id)
    db.add(friendUser)
    db.add(userFriend)
    await db.commit()
    await db.refresh(friendUser)
    await db.refresh(userFriend)

