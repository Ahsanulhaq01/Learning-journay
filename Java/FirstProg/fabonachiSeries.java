class Fibonacchi{
    public static void main(String[] args) {
        int a = 5;
        int value = fibo(a);

        System.out.println("The fibonacchi Series for " + a + " is : " +value);
    }

    public static int fibo(int a){
        if(a <= 1)return  a;

        return fibo(a-1) + fibo(a-2);
    }
}