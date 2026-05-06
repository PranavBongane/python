from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate

app = FastAPI()

text_post ={1: {"id": 1, "title": "First Post", "content": "This is the content of the first post."},
            2: {"id": 2, "title": "Second Post", "content": "This is the content of the second post."},
            3: {"id": 3, "title": "Third Post", "content": "This is the content of the third post."},
            4: {"id": 4, "title": "Fourth Post", "content": "This is the content of the fourth post."},
            5: {"id": 5, "title": "Fifth Post", "content": "This is the content of the fifth post."},
            6: {"id": 6, "title": "Sixth Post", "content": "This is the content of the sixth post."},
            7: {"id": 7, "title": "Seventh Post", "content": "This is the content of the seventh post."},
            8: {"id": 8, "title": "Eighth Post", "content": "This is the content of the eighth post."},
            9: {"id": 9, "title": "Ninth Post", "content": "This is the content of the ninth post."},
            10: {"id": 10, "title": "Tenth Post", "content": "This is the content of the tenth post."}}

@app.get("/posts")
def get_post(limit: int = None):
    if limit is not None:
        return list(text_post.values())[:limit]
    return text_post

@app.get("/posts/{id}")
def get_post_by_id(id: int):
    if id in text_post:
        return text_post[id]
    else:
        raise HTTPException(status_code=404, detail="Post not found")
    
@app.post("/posts") 
def create_post(post: PostCreate) -> PostCreate:
    new_id = max(text_post.keys()) + 1
    new_post = {"id": new_id, "title": post.title, "content": post.content}
    text_post[new_id] = new_post
    return new_post
