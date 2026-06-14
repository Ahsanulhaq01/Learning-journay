import java.util.Scanner;

public class SwitchdecisionStructure {
    public static void main(String[] args) {
        System.out.println("Enter you grade");
        Scanner scanner = new Scanner(System.in);
        String grade = scanner.next();
        scanner.close();
        String message;
        switch (grade){
            case "A":
                message = "excellent job";
                System.out.println(message);
                break;
            case "B":
                message = "great job";
                System.out.println(message);
                break;
            case "C":
                message = "good jon";
                System.out.println(message);
                break;
            default:
                System.out.println("you are faild ");



        }
    }
}
