package decision_structure;

import java.util.Scanner;

public class nestedDecision_structure {
     static void main(String[] args){
        System.out.println("Enter your score");
        Scanner scanner = new Scanner(System.in);
        double score = scanner.nextDouble();
        char grade = 0;
        if(score < 60){
            grade = 'F';
        }
        else if(score < 70){
            grade = 'D';
        }
        else if(score < 80){
            grade = 'C';
        }
        else if(score < 90){
            grade = 'B';
        }
        else if(score >= 90){
            grade = 'A';
        }
        System.out.println("Your grade as : " + grade);
                
    }
    
}
