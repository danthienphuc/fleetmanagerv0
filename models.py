from unicodedata import name
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Fleet(Base):
    __tablename__ = "fleets"

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(100), nullable=False)


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(100), nullable=False)

    fleet_id = Column(Integer, ForeignKey("fleets.id"))
    
class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(100), nullable=False)

class Route(Base):
    __tablename__ = "routes"

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(100), nullable=False)

class RouteDetails(Base):
    __tablename__ = "routedetails"

    route_id = Column(Integer, ForeignKey("routes.id"))
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    driver_id = Column(Integer, ForeignKey("drivers.id"))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
