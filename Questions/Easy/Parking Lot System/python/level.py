from typing import List

from models.vehicle import Vehicle
from parking_spot import ParkingSpot


class Level:
    def __init__(self, floor, capacity):
        self.floor = floor
        self.parking_spots: List[ParkingSpot] = [ParkingSpot(idx) for idx in range(capacity)]

    def park(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            if spot.is_available():
                spot.park_vehicle(vehicle)
                return True
        return False

    def un_park(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            if not spot.is_available() and spot.get_parked_vehicle() == vehicle:
                spot.unpark_vehicle()
                return True
        return False

    def display_available(self):
        print(f"Level {self.floor} status with : ")
        for spot in self.parking_spots:
            print(f"Spot {spot.get_spot_number()}: {'Available' if spot.is_available() else 'Occupied'}")
