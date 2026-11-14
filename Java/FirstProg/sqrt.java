import java.util.Scanner;

public class sqrt {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a Number to calculate it's square Root : ");
        int number = scanner.nextInt();
        scanner.close();
        int value = squareRoot(number);
        System.out.println("The square Root of "+ number + " is : " + value);
    }


    public static int squareRoot(int number){
        return number * number;
    }
}
