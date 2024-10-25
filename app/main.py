from fastapi import FastAPI
from app.routers import nasa_apis

app = FastAPI(title='NASA ETL Project')

app.include_router(nasa_apis.router)

@app.get("/")
async def root():
  return {"message": "NASA ETL Project API"}