import java.util.Arrays;

class CustomArrayGen<T>{
    
   private Object[] data;
   private  static int DEFAULT_SIZE = 10;
   private int size = 0;


   public  CustomArrayGen(){
        this.data = new Object[DEFAULT_SIZE];
   }


   public void add(T num){
    if(isFull()){
        resize();
    }

    data[size++] = num;
    

   }

   public Object remove(){
        Object removeelement = data[size];
        size--;
        return removeelement;
   }

   public boolean isEmpty(){
    return size == 0;
   }

   public int size(){
    return size;
   }



   private boolean isFull(){
    if(size == DEFAULT_SIZE) return true;

    return false;
   }

   private void resize(){
    Object[] temp = new Object[data.length * 2];

    for(int i =0; i < data.length ; i++){
        temp[i] = data[i];


    }

    data = temp;

   }


   public Object get(int index){
     return data[index];
   }

   public void set(int index , T value){
        data[index] = value;
   }
  

   @Override
   public String toString() {

       return "CustromArray {data = " + Arrays.toString(data) + ", size = "+ size + "}";
    //    return Arrays.toString(data);
   }
     
}