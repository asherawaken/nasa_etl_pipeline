from fastapi import APIRouter
from app.utils import fetch_data

router = APIRouter(prefix="/nasa", tags=["NASA"])

@router.get("/apod")
async def get_apod_data(start_date: str, end_date: str):
    data = fetch_data.fetch_apod_data(start_date, end_date)
    return data

@router.get("/neo")
async def get_neo_data(start_date: str, end_date: str):
    data = fetch_data.fetch_neo_data(start_date, end_date)
    return data

@router.get("/mars_photos")
async def get_mars_photos(earth_date: str):
    data = fetch_data.fetch_mars_photos(earth_date)
    return data