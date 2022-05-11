from unicodedata import name
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Fleet(Base):
    __tablename__ = "fleets"

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(100), index=True)


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(100), index=True)

    fleet_id = Column(Integer, ForeignKey("fleets.id"))
    
class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(100), index=True)

class Route(Base):
    __tablename__ = "routes"

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(100), index=True)

class RouteDetails(Base):
    __tablename__ = "routedetails"

    route_id = Column(Integer, ForeignKey("routes.id"), primary_key=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), primary_key=True)
    driver_id = Column(Integer, ForeignKey("drivers.id"))
    