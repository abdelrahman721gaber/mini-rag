# it must contain route of welcome
from fastapi import FastAPI, APIRouter, Depends
import os
from helpers.config import get_settings, Settings


base_router = APIRouter(
    prefix="/api/v1",
    tags=["api version 1"],  # it's tags not tag
)


@base_router.get("/welcome")
async def welcom(app_settings: Settings = Depends(get_settings)):  # to handle multiple requiests
    #app_settings = get_settings()
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION

    return {"app_name": app_name, "app_verison": app_version}
