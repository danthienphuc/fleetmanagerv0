from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Fleet

# Create a fleet
@app.post("/fleet/", response_model=schemas.Fleet)
async def create_fleet(fleet:schemas.Fleet,db: Session = Depends(get_db)):
    fleet = await crud.create_fleet(db=db, fleet=fleet)
    return fleet
    
# Get all fleets
@app.get("/fleets/", response_model=list[schemas.Fleet])
async def get_fleets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_fleets(db=db, skip=skip, limit=limit)

# Get a fleet
@app.get("/fleet/{fleet_id}", response_model=schemas.Fleet)
async def get_fleet(fleet_id: int, db: Session = Depends(get_db)):
    return crud.get_fleet(db=db, fleet_id=fleet_id)

# Update a fleet
@app.put("/fleet/{fleet_id}", response_model=schemas.Fleet)
async def update_fleet(fleet_id: int, fleet: schemas.Fleet, db: Session = Depends(get_db)):
    return crud.update_fleet(db=db, fleet_id=fleet_id, fleet=fleet)

# Delete a fleet
@app.delete("/fleet/{fleet_id}", response_model=schemas.Fleet)
async def delete_fleet(fleet_id: int, db: Session = Depends(get_db)):
    return crud.delete_fleet(db=db, fleet_id=fleet_id)

# Vehicle

# Create a vehicle
@app.post("/vehicle/", response_model=schemas.Vehicle)
async def create_vehicle(vehicle:schemas.Vehicle,db: Session = Depends(get_db)):
    vehicle = await crud.create_vehicle(db=db, vehicle=vehicle)
    return vehicle

# Get all vehicles
@app.get("/vehicles/", response_model=list[schemas.Vehicle])
async def get_vehicles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_vehicles(db=db, skip=skip, limit=limit)

# Get a vehicle
@app.get("/vehicle/{vehicle_id}", response_model=schemas.Vehicle)
async def get_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    return crud.get_vehicle(db=db, vehicle_id=vehicle_id)

# Update a vehicle
@app.put("/vehicle/{vehicle_id}", response_model=schemas.Vehicle)
async def update_vehicle(vehicle_id: int, vehicle: schemas.Vehicle, db: Session = Depends(get_db)):
    return crud.update_vehicle(db=db, vehicle_id=vehicle_id, vehicle=vehicle)

# Delete a vehicle
@app.delete("/vehicle/{vehicle_id}", response_model=schemas.Vehicle)
async def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    return crud.delete_vehicle(db=db, vehicle_id=vehicle_id)

# Driver

# Create a driver
@app.post("/driver/", response_model=schemas.Driver)
async def create_driver(driver:schemas.Driver,db: Session = Depends(get_db)):
    driver = await crud.create_driver(db=db, driver=driver)
    return driver

# Get all drivers
@app.get("/drivers/", response_model=list[schemas.Driver])
async def get_drivers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_drivers(db=db, skip=skip, limit=limit)

# Get a driver
@app.get("/driver/{driver_id}", response_model=schemas.Driver)
async def get_driver(driver_id: int, db: Session = Depends(get_db)):
    return crud.get_driver(db=db, driver_id=driver_id)

# Update a driver
@app.put("/driver/{driver_id}", response_model=schemas.Driver)
async def update_driver(driver_id: int, driver: schemas.Driver, db: Session = Depends(get_db)):
    return crud.update_driver(db=db, driver_id=driver_id, driver=driver)

# Delete a driver
@app.delete("/driver/{driver_id}", response_model=schemas.Driver)
async def delete_driver(driver_id: int, db: Session = Depends(get_db)):
    return crud.delete_driver(db=db, driver_id=driver_id)

# Route

# Create a route
@app.post("/route/", response_model=schemas.Route)
async def create_route(route:schemas.Route,db: Session = Depends(get_db)):
    route = await crud.create_route(db=db, route=route)
    return route

# Get all routes
@app.get("/routes/", response_model=list[schemas.Route])
async def get_routes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_routes(db=db, skip=skip, limit=limit)

# Get a route
@app.get("/route/{route_id}", response_model=schemas.Route)
async def get_route(route_id: int, db: Session = Depends(get_db)):
    return crud.get_route(db=db, route_id=route_id)

# Update a route
@app.put("/route/{route_id}", response_model=schemas.Route)
async def update_route(route_id: int, route: schemas.Route, db: Session = Depends(get_db)):
    return crud.update_route(db=db, route_id=route_id, route=route)

# Delete a route
@app.delete("/route/{route_id}", response_model=schemas.Route)
async def delete_route(route_id: int, db: Session = Depends(get_db)):
    return crud.delete_route(db=db, route_id=route_id)

# RouteDetail

# Create a route detail
@app.post("/routedetail/", response_model=schemas.RouteDetail)
async def create_routedetail(routedetail:schemas.RouteDetail,db: Session = Depends(get_db)):
    routedetail = await crud.create_routedetail(db=db, routedetail=routedetail)
    return routedetail

# Get all route details
@app.get("/routedetails/", response_model=list[schemas.RouteDetail])
async def get_route_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_route_details(db=db, skip=skip, limit=limit)

# Get a route detail
@app.get("/routedetail/{route_detail_id}", response_model=schemas.RouteDetail)
async def get_route_detail(route_detail_id: int, db: Session = Depends(get_db)):
    return crud.get_route_detail(db=db, route_detail_id=route_detail_id)

# Update a route detail
@app.put("/routedetail/{route_detail_id}", response_model=schemas.RouteDetail)
async def update_route_detail(route_detail_id: int, route_detail: schemas.RouteDetail, db: Session = Depends(get_db)):
    return crud.update_route_detail(db=db, route_detail_id=route_detail_id, route_detail=route_detail)

# Delete a route detail
@app.delete("/routedetail/{route_detail_id}", response_model=schemas.RouteDetail)
async def delete_route_detail(route_detail_id: int, db: Session = Depends(get_db)):
    return crud.delete_route_detail(db=db, route_detail_id=route_detail_id)


