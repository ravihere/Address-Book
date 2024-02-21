# database/models.py

from sqlalchemy import Column, Integer, Float, String
from database import Base
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)


class Address(Base):
    """
    Address model.
    """
    __tablename__ = "address_book"

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    name = Column(String)

    def __repr__(self):
        return f"<Address id={self.id}, name={self.name}>"


logger.info("Database models loaded.")


class AddressBase(BaseModel):
    """
    Base model for Address.
    """
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    name: str


class AddressCreate(AddressBase):
    """
    Model for creating a new Address.
    """
    pass


class AddressUpdate(AddressBase):
    """
    Model for updating an existing Address.
    """
    pass


class AddressInDB(AddressBase):
    """
    Model for Address with ID.
    """
    id: int

    class Config:
        from_attributes = True
