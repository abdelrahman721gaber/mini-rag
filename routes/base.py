# it must contain route of welcome
from fastapi import FastAPI, APIRouter
import os

base_router = APIRouter(
    prefix = '/api/v1',
    tags = ['api version 1'],    # it's tags not tag 
)

@base_router.get("/welcome")
async def welcom():   # to handle multiple requiests

    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    
    return {
        "app_name": app_name,
        "app_verison": app_version
        }