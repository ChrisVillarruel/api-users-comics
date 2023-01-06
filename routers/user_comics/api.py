from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from config.db import client as db

router = APIRouter()


class AddToLayaway(BaseModel):
    id_comic: int
    title: str
    image: str


class Layaway(BaseModel):
    list_layaway: list[AddToLayaway]
    user_id: str | None = None


@router.post("/addToLayaway/")
async def add_to_layaway(user_id: str, layaway: Layaway):
    my_db = db["comics"]
    my_collection_user_comics = my_db["user_comics"]
    my_collection_layaway_comics = my_db["layaway_comics"]
    user_db = my_collection_user_comics.find_one({"user_id": user_id})

    if not user_db:
        raise HTTPException(detail="Usuario no encontrado", status_code=400)
    elif not user_db.get("is_active"):
        raise HTTPException(detail="Usuario no activo", status_code=400)
    else:
        layaway.user_id = user_id
        my_collection_layaway_comics.insert_one(layaway.dict())
        return {"status": "Sus comics fueron apartados exitosamente"}
