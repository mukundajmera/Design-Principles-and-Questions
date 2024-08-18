from level import Level
from models.car import Car
from models.motorcycle import Motorcycle
from models.truck import Truck
from parking_lot import ParkingLot


class ParkingLotDemo:

    @staticmethod
    def run():
        parking_lot = ParkingLot.get_instance()
        parking_lot.add_level(Level(1, 5))
        parking_lot.add_level(Level(2, 15))

        car = Car("PY123")
        truck = Truck("KA789")
        motorcycle = Motorcycle("MH1")

        # Park vehicles
        parking_lot.park_vehicle(car)
        parking_lot.park_vehicle(truck)
        parking_lot.park_vehicle(motorcycle)

        parking_lot.park_vehicle(Motorcycle("MH2"))
        parking_lot.park_vehicle(Motorcycle("MH3"))
        parking_lot.park_vehicle(Motorcycle("MH4"))

        # Display availability
        parking_lot.display_availability()

        # Un park vehicle
        parking_lot.un_park_vehicle(car)

        # Display updated availability
        parking_lot.display_availability()


if __name__ == '__main__':
    ParkingLotDemo.run()
