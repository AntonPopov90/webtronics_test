
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from authentication.schemas import UserRead
from database import get_async_session
from database import post, User
from posts.schemas import PostCreate, PostEdit, PostRead

router = APIRouter(
    prefix='/posts',
    tags=["posts"]
)


@router.post("/add_post")
async def add_post(new_post: PostCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(post).values(**new_post.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get("/")
async def get_selected_post(posts: str, session: AsyncSession = Depends(get_async_session)):
    query = select(post).where(post.c.title == posts)
    result = await session.execute(query)
    return result.all()


@router.post("/edit_post")
async def edit_post(posts: int, post_edit: PostEdit, session: AsyncSession = Depends(get_async_session)):
    query = update(post).where(post.c.id == posts).values(**post_edit.dict())
    await session.execute(query)
    await session.commit()
    return {"status": "Post successfully edited"}


@router.post("/delete_post")
async def delete_post(posts: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(post).where(post.c.id == posts)
    await session.execute(stmt)
    await session.commit()
    return {"status": "Post successfully deleted"}


@router.post("/add_like")
async def add_like(user: UserRead, post_id: int,posts: PostRead, session: AsyncSession = Depends(get_async_session)):
    if user.id == posts.user_id:
        print(user)
        return {"status": f"You can't like your own post"}
    else:
        stmt = update(post).where(post.c.id == post_id).values({"likes": post.c.likes+1})
        await session.execute(stmt)
        await session.commit()
        print(user.id)
        print(posts.user_id)
        return {"status": f"You'd liked this post"}
