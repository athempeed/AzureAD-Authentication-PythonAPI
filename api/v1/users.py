from fastapi import APIRouter, Depends, HTTPException, Query
from api.schemas import user

router = APIRouter()
fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}

@router.get("/")
def Get():
    return fake_items_db