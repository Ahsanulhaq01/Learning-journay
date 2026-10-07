package interfaces;

/**
 * Car
 */
public class Car implements Brake , Engine ,Mediaplayer {

    @Override
    public void brake() {
        System.out.println("brake method of Brake ");
    }

    @Override
    public void start() {
        System.out.println("start method of engine");
    }
    
    @Override
    public void stop() {
        System.out.println("stop method of engine");
    }

    @Override
    public void acc() {
        System.out.println("acc method of engine");
    }

    @Override
    public void media() {
        System.out.println("media method of mediaPlayer");
    }
}