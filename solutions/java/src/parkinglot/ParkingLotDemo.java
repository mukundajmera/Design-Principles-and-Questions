package parkinglot;

import parkinglot.VehicleType.Car;
import parkinglot.VehicleType.Motorcycle;
import parkinglot.VehicleType.Truck;
import parkinglot.VehicleType.Vehicle;

public class ParkingLotDemo {

    public static void run(){
        //add logic for parking lot
        ParkingLot parkingLot = ParkingLot.getInstance();

        parkingLot.addLevel(new Level(1, 5));
        parkingLot.addLevel(new Level(2, 20));

        Vehicle car = new Car("KAHU1234");
        Vehicle truck = new Truck("KA511245");
        Vehicle bike = new Motorcycle("RJ140772");
        //Park vehicles
        parkingLot.parkVehicle(car);
        parkingLot.parkVehicle(truck);
        parkingLot.parkVehicle(bike);

        //check availability
        parkingLot.displayAvailability();

        // un park
        parkingLot.unparkVehicle(car);

        //check availability
        parkingLot.displayAvailability();
    }
}

