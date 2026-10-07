package interfaces;
public class Main {
    public static void main(String[] args) {
        Car obj = new Car();

        obj.acc();
        obj.brake();
        obj.start();
        obj.stop();
        obj.media();

        System.out.println("hello from main class");

        System.out.println();
        Jeep jeep = new Jeep();

        jeep.brake();
        jeep.start();
        jeep.stop();
        jeep.acc();
    }
}
