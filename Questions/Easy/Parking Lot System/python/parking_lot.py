from typing import List

from level import Level
from models.vehicle import Vehicle


class ParkingLot:
    _instance = None

    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("Cannot create multiple class parking lots.")
        else:
            ParkingLot._instance = self
            self.levels: List[Level] = []

    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot()
        return ParkingLot._instance

    def add_level(self, level: Level):
        self.levels.append(level)

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        """
        Parking in any First come first server level
        :param vehicle:
        :return: bool of success or not
        """
        for level in self.levels:
            if level.park(vehicle):
                return True
        return False

    def un_park_vehicle(self, vehicle: Vehicle) -> bool:
        """
        Unpark vehicle for any level it is listed on
        :param vehicle:
        :return: bool of success or not
        """
        for level in self.levels:
            if level.un_park(vehicle):
                return True
        return False

    def display_availability(self) -> None:
        for level in self.levels:
            level.display_available()
