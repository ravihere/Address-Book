# api/crud.py
import logging
from typing import Type
from fastapi import HTTPException
from sqlalchemy.orm import Session
from database.models import Address
from database.models import AddressCreate, AddressInDB, AddressUpdate
from geopy.distance import geodesic

logger = logging.getLogger(__name__)


def create_address(db: Session, address: AddressCreate) -> AddressInDB:
    """
    Create a new address and store it in databae.
    """
    try:
        db_address = Address(**address.dict())
        db.add(db_address)
        db.commit()
        db.refresh(db_address)
        logger.info(f"Address created: {db_address}")
        return db_address
    except Exception as e:
        logger.exception("Error occurred while creating address")
        raise HTTPException(status_code=500, detail="Internal server error")


def update_address(db: Session, address_id: int, address: AddressUpdate) -> Type[Address] | None:
    """
    Update an existing address by ID.
    """
    # Check if the address with the provided ID exists in the database
    db_address = db.query(Address).filter(Address.id == address_id).first()
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    try:
        # update the address
        for key, value in address.dict(exclude_unset=True).items():
            setattr(db_address, key, value)
        db.commit()
        db.refresh(db_address)
        logger.info(f"Address updated: {db_address}")
        return db_address
    except Exception as e:
        logger.exception("Error occurred while updating address")
        raise HTTPException(status_code=500, detail="Internal server error")


def delete_address(db: Session, address_id: int):
    """
    Delete an address by ID.
    """
    db_address = db.query(Address).filter(Address.id == address_id).first()
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    try:

        db.delete(db_address)
        db.commit()
        logger.info(f"Address deleted with ID: {address_id}")
        return {"message": "Address deleted successfully"}
    except Exception as e:
        logger.exception("Error occurred while deleting address")
        raise HTTPException(status_code=500, detail="Internal server error")


def get_all_addressess(db: Session) -> list:
    address_data = db.query(Address).all()
    return address_data


def retrieve_addresses_within_distance(db: Session, latitude: float, longitude: float, distance: float):
    try:
        addresses_within_distance = []

        # Retrieve all addresses from the database
        all_addresses = db.query(Address).all()

        # Define the reference point
        reference_point = (latitude, longitude)

        # Iterate over each address and calculate its distance from the reference point
        for address in all_addresses:
            address_point = (address.latitude, address.longitude)
            distance_between_points = geodesic(reference_point, address_point).kilometers

            # Check if the distance between points is within the given distance
            if distance_between_points <= distance:
                addresses_within_distance.append(address)

        # Log the number of addresses found within the given distance
        logger.info(
            f"{len(addresses_within_distance)} addresses found within {distance} kilometers from "
            f"(latitude: {latitude}, longitude: {longitude})")

        return addresses_within_distance
    except Exception as e:
        logger.exception("Error occurred while retrieving addresses within distance")
        raise HTTPException(status_code=500, detail="Internal server error")
