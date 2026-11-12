class OddEven{
    public static void main(String[] args) {
        int a  = 1;
        String value = oddEven(a);
        System.out.println(value);
    }

    public static String oddEven(int a){
        if((a & 1) == 0)return "The number is Even";
        return "The Number is Odd";
    }
}