from calendar import c
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()


class Fleet(BaseModel):
    __tablename__ = "fleets"
    id = Column(Integer, primary_key=True)
    name = Column(String (50), nullable=False)
    
class Vehicle(BaseModel):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True)
    name = Column(String (50), nullable=False)
    fleet_id = Column(Integer, ForeignKey("fleets.id"))

class Driver(BaseModel):
    __tablename__ = "drivers"
    id = Column(Integer, primary_key=True)
    name = Column(String (50), nullable=False)
    
class Route(BaseModel):
    __tablename__ = "routes"
    id = Column(Integer, primary_key=True)
    name = Column(String (50), nullable=False)
        
    