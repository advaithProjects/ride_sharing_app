from fastapi import FastAPI, HTTPException

from models.user import Rider, Driver
from services.ride_service import RideService
from services.fare_strategy import NormalFare

from schemas.ride_schema import RideRequest, RideResopnce

app = FastAPI()

fare_strategy = NormalFare()
ride_service = RideService(fare_strategy)

# register dummy driver
driver1 = Driver("D1", "Advaith", "9441042831")
ride_service.register_driver(driver1)


@app.post("/request-ride", response_model=RideResopnce)
def request_ride(request: RideRequest):
    rider = Rider(request.ride_id, request.rider_name, request.phone)
    try:
        ride = rider.request_ride(ride_service, request.distance)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return RideResopnce(
        ride_id=ride.ride_id,
        driver_name=ride.driver.name,
        fare=ride.fare,
        status=ride.status,
    )


@app.get("/ride/{ride_id}", response_model=RideResopnce)
def get_ride(ride_id: str):
    ride = ride_service.get_ride(ride_id)

    if not ride:
        raise HTTPException(status_code=404, detail="Ride not found")
    return RideResopnce(
        ride_id=ride.ride_id,
        driver_name=ride.driver.name,
        fare=ride.fare,
        status=ride.status,
    )


# To Run this code type in terminal (python -m uvicorn main:app --reload)
# http:127.0.0.1:8000/docs
