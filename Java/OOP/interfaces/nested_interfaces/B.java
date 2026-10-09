package nested_interfaces;

public class B implements A.InnerA{
    public void  fun(){
        System.out.println("hello from override method fun");
    }

    public void greeting(){
        System.out.println("hello through object B");
    }
}
