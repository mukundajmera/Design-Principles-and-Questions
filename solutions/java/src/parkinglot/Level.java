package parkinglot;

import parkinglot.VehicleType.Vehicle;

import java.util.ArrayList;
import java.util.List;

public class Level {
    private final int floor;
    private final List<ParkingSpot> parkingSpot;

    public Level(int floor, int numberSpots) {
        this.floor = floor;
        this.parkingSpot = new ArrayList<>(numberSpots);
        for(int i = 0; i < numberSpots; i++) {
            parkingSpot.add(new ParkingSpot(i));
        }
    }

    public synchronized boolean parkVehicle(Vehicle vehicle) {
        for(ParkingSpot spot : parkingSpot) {
            if(spot.isAvailable()){
                spot.parkVehicle(vehicle);
                return true;
            }
        }
        return false;
    }

    public synchronized boolean unparkVehicle(Vehicle vehicle) {
        for (ParkingSpot spot : parkingSpot) {
            if (!spot.isAvailable() && spot.getParkedVehicle().equals(vehicle)) {
                spot.unparkVehicle();
                return true;
            }
        }
        return false;
    }

    public void displayAvailability(){
        System.out.println("Level "+ floor + " Availability");
        for(ParkingSpot spot : parkingSpot) {
            System.out.println("Spot " + spot.getSpotNumber() + ": " + (spot.isAvailable() ? "Available" : "Occupied"));
        }
    }

}
