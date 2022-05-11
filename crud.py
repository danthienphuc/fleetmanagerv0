import fastapi
from sqlalchemy.orm import Session
from fastapi import HTTPException

import models, schemas

# CRUD operations for Fleet
def create_fleet(db: Session, fleet: schemas.FleetCreate):
    db_fleet = models.Fleet(name=fleet.name)
    db.add(db_fleet)
    db.commit()
    db.refresh(db_fleet)
    return db_fleet

def get_fleets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Fleet).offset(skip).limit(limit).all()

def get_fleet(db: Session, fleet_id: int):
    return db.query(models.Fleet).filter(models.Fleet.id == fleet_id).first()

def update_fleet(db: Session, fleet_id: int, fleet: schemas.Fleet):
    db_fleet = get_fleet(db, fleet_id)
    if db_fleet:
        db_fleet.name = fleet.name
        db.commit()
        db.refresh(db_fleet)
        return db_fleet
    else:
        raise HTTPException(status_code=404, detail="Fleet not found")

def delete_fleet(db: Session, fleet_id: int):
    db_fleet = get_fleet(db, fleet_id)
    if db_fleet:
        db.delete(db_fleet)
        db.commit()
        return db_fleet
    else:
        raise HTTPException(status_code=404, detail="Fleet not found")

# CRUD operations for Vehicle
def create_vehicle(db: Session, vehicle: schemas.VehicleCreate):
    db_vehicle = models.Vehicle(**vehicle.dict())
    db.add(db_vehicle) 
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

def get_vehicles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vehicle).offset(skip).limit(limit).all()

def get_vehicle(db: Session, vehicle_id: int):
    return db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()

def update_vehicle(db: Session, vehicle_id: int, vehicle: schemas.Vehicle):
    db_vehicle = get_vehicle(db, vehicle_id)
    if db_vehicle:
        db_vehicle.name = vehicle.name
        db.commit()
        db.refresh(db_vehicle)
        return db_vehicle
    else:
        raise HTTPException(status_code=404, detail="Vehicle not found")

def delete_vehicle(db: Session, vehicle_id: int):
    db_vehicle = get_vehicle(db, vehicle_id)
    if db_vehicle:
        db.delete(db_vehicle)
        db.commit()
        return db_vehicle
    else:
        raise HTTPException(status_code=404, detail="Vehicle not found")

# CRUD operations for Driver
def create_driver(db: Session, driver: schemas.DriverCreate):
    db_driver = models.Driver(**driver.dict())
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver

def get_driver(db: Session, driver_id: int):
    return db.query(models.Driver).filter(models.Driver.id == driver_id).first()

def get_drivers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Driver).offset(skip).limit(limit).all()

def update_driver(db: Session, driver_id: int, driver: schemas.Driver):
    db_driver = get_driver(db, driver_id)
    if db_driver:
        db_driver.name = driver.name
        db.commit()
        db.refresh(db_driver)
        return db_driver
    else:
        raise HTTPException(status_code=404, detail="Driver not found")

def delete_driver(db: Session, driver_id: int):
    db_driver = get_driver(db, driver_id)
    if db_driver:
        db.delete(db_driver)
        db.commit()
        return db_driver
    else:
        raise HTTPException(status_code=404, detail="Driver not found")
    

# CRUD operations for Route
def create_route(db: Session, route: schemas.RouteCreate):
    db_route = models.Route(**route.dict())
    db.add(db_route)
    db.commit()
    db.refresh(db_route)
    return db_route

def get_route(db: Session, route_id: int):
    return db.query(models.Route).filter(models.Route.id == route_id).first()

def get_routes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Route).offset(skip).limit(limit).all()

def update_route(db: Session, route_id: int, route: schemas.Route):
    db_route = get_route(db, route_id)
    if db_route:
        db_route.name = route.name
        db.commit()
        db.refresh(db_route)
        return db_route
    else:
        raise HTTPException(status_code=404, detail="Route not found")

def delete_route(db: Session, route_id: int):
    db_route = get_route(db, route_id)
    if db_route:
        db.delete(db_route)
        db.commit()
        return db_route
    else:
        raise HTTPException(status_code=404, detail="Route not found")

# CRUD operations for RouteDetail
def create_route_detail(db: Session, route_detail: schemas.RouteDetailCreate):
    db_route_detail = models.RouteDetail(**route_detail.dict())
    db.add(db_route_detail)
    db.commit()
    db.refresh(db_route_detail)
    return db_route_detail

def get_route_detail(db: Session, route_id: int,vehicle_id: int):
    return db.query(models.RouteDetail).filter(models.RouteDetail.route_id == route_id,models.RouteDetail.vehicle_id ==vehicle_id).first()

def get_route_details(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.RouteDetail).offset(skip).limit(limit).all()

def update_route_detail(db: Session, route_detail_id: int, route_detail: schemas.RouteDetail):
    db_route_detail = get_route_detail(db, route_detail_id)
    if db_route_detail:
        db_route_detail.name = route_detail.name
        db.commit()
        db.refresh(db_route_detail)
        return db_route_detail
    else:
        raise HTTPException(status_code=404, detail="RouteDetail not found")

def delete_route_detail(db: Session, route_id: int,vehicle_id: int):
    db_route_detail = get_route_detail(db, route_id, vehicle_id)
    if db_route_detail:
        db.delete(db_route_detail)
        db.commit()
        return db_route_detail
    else:
        raise HTTPException(status_code=404, detail="RouteDetail not found")

