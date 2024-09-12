from models.vehicle import Vehicle
from models.vehicle_type import VehicleType


class ParkingSpot:
    def __init__(self, spot_number: int):
        self.spot_number = spot_number
        self.parked_vehicle = None

    def is_available(self) -> bool:
        return self.parked_vehicle is None

    def park_vehicle(self, vehicle: Vehicle):
        if self.is_available():
            self.parked_vehicle = vehicle
        else:
            raise ValueError("Spot not available")

    def unpark_vehicle(self):
        self.parked_vehicle = None

    def get_vehicle_type(self) -> VehicleType:
        return self.parked_vehicle.vehicle_type

    def get_parked_vehicle(self) -> Vehicle:
        return self.parked_vehicle

    def get_spot_number(self) -> int:
        return self.spot_number
