from fastapi import APIRouter, Depends, HTTPException, Query


router = APIRouter()
fake_items_db = {"employee": [{"name": "Plumbus"},{"name": "Portal Gun"},{"name": "Jack"}]}

@router.get("/")
def Get():
    return fake_items_db