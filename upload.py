from typing import Union
from typing import Annotated

from fastapi.responses import HTMLResponse

from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int



# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


@app.get("/user/{user_id}")
def read_user(user_id: int, user_name: str, user_age: int):
    return {"user_id": user_id, "user_name": user_name, "user_age": user_age}


@app.put("/users/{user_id}")
def update_user(user_id:int, user: User):
    return {"user_name": user.name,"user_age": user.age, "user_id":user_id}

@app.post("/users/")
async def create_user(user: User):
    return user



# POST FILES
@app.post("/uploadfile/")
async def create_upload_file(
    file: Annotated[UploadFile, File(description="A file read as UploadFile")],
):
    return {"filename": file.filename}

@app.get("/")
async def main():
    content = """
<body>
<form action="/uploadfile/" enctype="multipart/form-data" method="post">
<input name="file" type="file" >
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)