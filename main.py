# main.py

import logging
from fastapi import FastAPI
from api.urls import router as api_router
from database import engine, Base

# Configure logging
logging.basicConfig(filename="address_book.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(api_router)

# Create tables
Base.metadata.create_all(bind=engine)
