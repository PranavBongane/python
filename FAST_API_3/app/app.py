from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select
from app.db import Post, create_tables, get_db

import shutil
import os
import tempfile
import requests
import base64


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)


# 🔹 ImageKit Upload Function (REST API)
def upload_to_imagekit(file_path, file_name):
    url = "https://upload.imagekit.io/api/v1/files/upload"

    with open(file_path, "rb") as f:
        encoded_file = base64.b64encode(f.read()).decode()

    payload = {
        "file": encoded_file,
        "fileName": file_name,
        "useUniqueFileName": True,
        "tags": ["backend-upload"]
    }

    private_key = os.getenv("IMAGEKIT_PRIVATE_KEY")
    auth = base64.b64encode(f"{private_key}:".encode()).decode()

    headers = {
        "Authorization": f"Basic {auth}"
    }

    response = requests.post(url, data=payload, headers=headers)
    return response.json()


# 🔹 Upload API
@app.post("/upload")
async def upload(
    file: UploadFile = File(...),
    caption: str = Form(...),
    session: AsyncSession = Depends(get_db)
):
    temp_file_path = None

    try:
        # create temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp_file:
            temp_file_path = temp_file.name
            shutil.copyfileobj(file.file, temp_file)

        # upload to imagekit
        upload_result = upload_to_imagekit(temp_file_path, file.filename)

        # check upload success
        if "url" not in upload_result:
            raise Exception(f"Upload failed: {upload_result}")

        # save to DB
        post = Post(
            caption=caption,
            url=upload_result["url"],
            file_type="video" if file.content_type.startswith("video/") else "image",
            file_name=upload_result["name"]
        )

        session.add(post)
        await session.commit()
        await session.refresh(post)

        return post

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if temp_file_path and os.path.exists(temp_file_path):
            os.unlink(temp_file_path)
        file.file.close()


# 🔹 Feed API
@app.get("/feed")
async def get_feed(session: AsyncSession = Depends(get_db)):
    result = await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts = [row[0] for row in result.all()]

    post_data = []
    for post in posts:
        post_data.append({
            "id": str(post.id),
            "caption": post.caption,
            "url": post.url,
            "file_type": post.file_type,
            "file_name": post.file_name,
            "created_at": post.created_at.isoformat()
        })

    return {"posts": post_data}