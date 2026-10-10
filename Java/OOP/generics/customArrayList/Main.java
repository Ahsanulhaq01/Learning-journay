public class Main {
    public static void main(String[] args) {
        // CustomArray obj = new CustomArray();
        WildCardexample<Integer> obj = new WildCardexample<>();

        // obj.add(10.2);
        obj.add(20);
        obj.add(30);

        System.out.println(obj.size());
        System.out.println(obj.isEmpty());

        System.out.println(obj.remove());

        System.out.println(obj.size());
        System.out.println(obj.isEmpty());

        System.out.println(obj.toString());
    }
}
