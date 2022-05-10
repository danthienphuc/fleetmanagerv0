from typing import Optional

from pydantic import BaseModel

# Fleet schema
class FleetBase(BaseModel):
    name: str

class FleetCreate(FleetBase):
    pass

class Fleet(FleetBase):
    id: int
    vehicle:list[Vehicle] = []

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

# Route Details schema

class RouteDetailsBase(BaseModel):
    pass

class RouteDetailsCreate(RouteDetailsBase):
    pass

class RouteDetails(RouteDetailsBase):
    route_id: int
    vehicle_id: int
    driver_id: int






# Item schema
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True