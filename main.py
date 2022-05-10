import re
from this import d
from fastapi import APIRouter, FastAPI, HTTPException
from fastapi_sqlalchemy import DBSessionMiddleware,db

from models import *

app = FastAPI()


# Create a router for the API
app.add_middleware(DBSessionMiddleware, db_url="psql://postgres:1@localhost:5432/postgres")

# Fleet API

# Get a list of all fleets
@app.get("/fleets")
def get_fleets():
    return db.query(Fleet).all()

# Get a fleet by id
@app.get("/fleets/{id}")
def get_fleets_by_id(id):
    f = db.session.get(Fleet, id=id)
    if not f:
        raise HTTPException(status_code=404, detail="Fleet not found")
    return f

# Create a new fleet
@app.post("/fleets",response_model=Fleet)
def create_fleet(fleet: Fleet):
    db.session.add(fleet)
    db.session.commit()
    return "Fleet created"

# Update a fleet
@app.patch("/fleets/{id}",response_model=Fleet)
def update_fleet(id:int, fleet: Fleet):
        f = db.session.get(Fleet, id)
        if not f:
            raise HTTPException(status_code=404, detail="Fleet not found")
        data = fleet.dict(exclude_unset=True)
        for key, value in data.items():
            setattr(f, key, value)
        db.session.add(f)
        db.session.commit()
        db.session.refresh(f)
        return f

# Delete a fleet
@app.delete("/fleets/{id}")
def delete_fleet(id: int):
    db.delete(db.query(Fleet).where(Fleet.id == id).first())
    return "Fleet deleted"

# Vehicle API

# Get a list of all vehicles
@app.get("/vehicles")
def get_vehicles():
    return db.query(Vehicle).all()

# Get a vehicle by id
@app.get("/vehicles/{id}")
def get_vehicle(id: int):
    return db.query(Vehicle).where(Vehicle.id == id).first()

# Create a new vehicle
@app.post("/vehicles",response_model=Vehicle)
def create_vehicle(vehicle: Vehicle):
    db.add(vehicle)
    db.commit()
    return "Vehicle created"

# Update a vehicle
@app.patch("/vehicles/{id}",response_model=Vehicle)
def update_vehicle(id: int, vehicle: Vehicle):
    db.update(vehicle)
    db.commit()