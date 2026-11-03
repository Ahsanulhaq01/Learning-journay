public  class Static {
    public static int a , b = 0;  // static block only load one time on the creation of first object of the class

    static{  //this static block
        a = a++;
        b = b+= 4;
    }
    
}
