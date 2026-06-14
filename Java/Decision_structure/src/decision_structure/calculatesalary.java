package decision_structure;

import java.util.Scanner;

public class calculatesalary {
    public static void main(String[] args){
        double salary = 1000;
        int qoute = 10;
        int bonus = 200;

        System.out.println("Enter the sales that you get this week");
        Scanner scanner = new Scanner(System.in);
        int sales = scanner.nextInt();
        scanner.close();
        if(sales > qoute){
            salary += bonus;
        }
        System.out.println("Salary : " + salary);

    }
}
