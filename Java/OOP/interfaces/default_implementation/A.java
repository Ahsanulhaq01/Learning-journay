package default_implementation;

public interface A {
    default void fun(){
        System.out.println("hello from default implementation of abstract class");
    }
}
