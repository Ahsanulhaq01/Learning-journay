public class BoxWeight extends Box {
    int weight;

    BoxWeight(){
        this.weight = -1;
    }

    BoxWeight(int weight){
        this.weight = weight;
    }

    BoxWeight(int l , int h , int w , int weight){
        super(l, w, h);
        this.weight = weight;
    }
    
}
