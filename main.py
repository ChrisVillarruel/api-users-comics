from fastapi import FastAPI
from routers.user_comics.api import router

app = FastAPI()
app.include_router(router)


@app.get("/")
async def main():
    return {"status": "Pagina pricipal"}
