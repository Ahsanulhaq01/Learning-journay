package interfaces;

public class Jeep implements Brake , Engine {
    @Override
    public void brake() {
        System.out.println("in jeep class brake method");
    }

    @Override
    public void start() {
        System.out.println("in jeep class start method");
    }
    @Override
    public void stop() {
        System.out.println("in jeep class stop method");
    }

    @Override
    public void acc() {
        System.out.println("in jeep class acc method");
    }
}

