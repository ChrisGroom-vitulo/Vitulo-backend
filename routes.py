from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class Cattle(BaseModel):
    id: int
    tag_number: str
    breed: str
    purchase_price: float
    farm: str
    sex: Optional[str]
    dob: Optional[str]

fake_db = []

@router.post("/cattle/", response_model=Cattle)
def add_cattle(cow: Cattle):
    fake_db.append(cow)
    return cow

@router.get("/cattle/", response_model=List[Cattle])
def get_all():
    return fake_db
