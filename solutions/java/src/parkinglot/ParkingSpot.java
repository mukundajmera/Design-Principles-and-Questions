package parkinglot;

import parkinglot.VehicleType.Vehicle;
import parkinglot.VehicleType.VehicleType;

public class ParkingSpot {

    private final int spotNumber;
    private VehicleType vehicleType;
    private Vehicle parkedVehicle;

    public ParkingSpot(int spotNumber) {
        this.spotNumber = spotNumber;
    }

    public synchronized boolean isAvailable(){
        return parkedVehicle == null;
    }

    public synchronized void parkVehicle(Vehicle vehicle) {
        if(isAvailable() ){
            parkedVehicle = vehicle;
            vehicleType = vehicle.getType();
        }else{
            throw new IllegalArgumentException("Already occupied the parking spot");
        }
    }

    public synchronized void unparkVehicle() {
        parkedVehicle = null;
        vehicleType = null;
    }

    public VehicleType getVehicleType() {
        return vehicleType;
    }

    public Vehicle getParkedVehicle() {
        return parkedVehicle;
    }

    public int getSpotNumber() {
        return spotNumber;
    }

}
