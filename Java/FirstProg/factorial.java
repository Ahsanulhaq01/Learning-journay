class Factorial{
    public static void main(String[] args) {
        int a = 5;
        int factorialValue = fact(a);
        System.out.println("factorial of " + a + " is : " + factorialValue);
    }
 
    public static int fact(int a){
        if(a <= 1)return 1;
        return a * fact(a- 1);
    }
}