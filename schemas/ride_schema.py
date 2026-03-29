from pydantic import BaseModel


class RideRequest(BaseModel):
    ride_id: str
    rider_name: str
    phone: str
    distance: float


class RideResopnse(BaseModel):
    ride_id: str
    driver_name: str
    fare: float
    status: str
