package decision_structure;

import java.util.Scanner;

public class qouteDecision {
    public static  void main(String[] args){
        int qoute = 10;

        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the sales count ");
        int sale = scanner.nextInt();
        scanner.close();
        if(sale>=qoute){
            System.out.println("Congratulation you have met the qoute");
        }
        else{
            int saleShort = qoute - sale;

            System.out.println("Sorry you did not get the qoute " + "You have " + saleShort + " saleShort");

        };
    }

}
