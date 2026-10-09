package nested_interfaces;

public class A {

    public interface InnerA {
    
        void fun();

        default void greeting(){
            System.out.println("Hello from default method in interfaces , greeting ");
        }
        
    }
} 