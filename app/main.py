from fastapi import FastAPI
from random import randint

from fastapi.responses import FileResponse

from fastapi.staticfiles import StaticFiles



app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def get_index_html():
    return FileResponse("static/index.html")



#12345




@app.get("/percentage")
async def get_random_percentage():
    return {'percentage': randint(0, 100)}


