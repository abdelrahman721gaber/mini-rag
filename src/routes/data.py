from fastapi import FastAPI, APIRouter, Depends, UploadFile
import os
from helpers.config import get_settings, Settings

base_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api version 1", "data"],  # it's tags not tag
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile,
                      app_settings: Settings = Depends(get_settings),
                      ):
    # Validata the file properities so we should put it in the controller directory
    