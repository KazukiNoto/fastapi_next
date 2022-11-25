from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# page hosting
app.mount("/", StaticFiles(directory="frontend/my-app/out", html=True), name="html")
