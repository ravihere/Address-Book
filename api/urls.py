# api/urls.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api import crud
from database import SessionLocal
from database.models import AddressCreate, AddressInDB, AddressUpdate, Address

router = APIRouter()


# Dependency to get the SQLAlchemy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/address/create/", response_model=AddressInDB)
def create_address(address: AddressCreate, db: Session = Depends(get_db)):
    """
    Create a new address.
    """
    return crud.create_address(db, address)


@router.put("/address/update/{address_id}", response_model=AddressInDB)
def update_address(address_id: int, address: AddressUpdate, db: Session = Depends(get_db)):
    """
    Update an existing address by ID.
    """
    return crud.update_address(db, address_id, address)


@router.delete("/address/delete/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    """
    Delete an address by ID.
    """
    return crud.delete_address(db, address_id)


@router.get("/address/nearby/")
def retrieve_addresses_within_distance(latitude: float, longitude: float, distance: float,
                                       db: Session = Depends(get_db)):
    """
    Retrieve addresses within a given distance from latitude and longitude.
    """
    return crud.retrieve_addresses_within_distance(db, latitude, longitude, distance)
