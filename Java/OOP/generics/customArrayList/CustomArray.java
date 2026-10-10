import java.util.Arrays;

class CustomArray{
    
   private int[] data;
   private  static int DEFAULT_SIZE = 10;
   private int size = 0;


   public  CustomArray(){
        this.data = new int[DEFAULT_SIZE];
   }


   public void add(int num){
    if(isFull()){
        resize();
    }

    data[size++] = num;
    

   }

   public int remove(){
        int removeelement = data[size];
        data[size] = 0;
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
    int[] temp = new int[data.length * 2];

    for(int i =0; i < data.length ; i++){
        temp[i] = data[i];


    }

    data = temp;

   }


   public int get(int index){
     return data[index];
   }

   public void set(int index , int value){
        data[index] = value;
   }
  

   @Override
   public String toString() {

       return "CustromArray {data = " + Arrays.toString(data) + ", size = "+ size + "}";
    //    return Arrays.toString(data);
   }
     
}