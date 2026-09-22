from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv(".env")

from source.routes.base import base_router  # Directly imports base_router

app = FastAPI()

# Use 'base_router' directly since you imported it by name
app.include_router(base_router)