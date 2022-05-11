from typing import Optional

from pydantic import BaseModel




# Fleet schema
class FleetBase(BaseModel):
    name: str

class FleetCreate(FleetBase):
    pass

class Fleet(FleetBase):
    id: int
    

    class Config:
        orm_mode = True

# Vehicle schema
class VehicleBase(BaseModel):
    name: str

class VehicleCreate(VehicleBase):
    pass

class Vehicle(VehicleBase):
    id: int
    fleet_id: int

    class Config:
        orm_mode = True

# Driver schema
class DriverBase(BaseModel):
    name: str

class DriverCreate(DriverBase):
    pass

class Driver(DriverBase):
    id: int

    class Config:
        orm_mode = True

# Route schema
class RouteBase(BaseModel):
    name: str

class RouteCreate(RouteBase):
    pass

class Route(RouteBase):
    id: int

    class Config:
        orm_mode = True

# Route Detail schema

class RouteDetailBase(BaseModel):
    pass

class RouteDetailCreate(RouteDetailBase):
    pass

class RouteDetail(RouteDetailBase):
    route_id: int
    vehicle_id: int
    driver_id: int