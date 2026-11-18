from typing import Literal

from pydantic import BaseModel


class AssetCreate(BaseModel):
    name: str
    category: str
    manufacturer: str | None = None
    model: str | None = None
    serial_number: str | None = None
    assigned_to: str | None = None
    status: Literal["available", "in_use", "repair", "retired"] = "available"
