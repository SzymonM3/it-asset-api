import sqlite3
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException

from database import create_asset, init_db
from schemas import AssetCreate


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="IT Asset Inventory API",
    description="A REST API for managing IT assets.",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/")
def read_root():
    return {"message": "IT Asset Inventory API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/assets", status_code=201)
def add_asset(asset: AssetCreate):
    try:
        return create_asset(asset.model_dump())

    except sqlite3.IntegrityError as exc:
        if "UNIQUE constraint failed: assets.serial_number" in str(exc):
            raise HTTPException(
                status_code=409,
                detail="An asset with this serial number already exists.",
            ) from exc

        raise
