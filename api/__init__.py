from fastapi import APIRouter

from api.v1 import users
from api.v1 import employees


api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(employees.router, prefix="/employees", tags=["employees"])