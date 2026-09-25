public class Box {
    int l;
    int w;
    int h;

    Box(){
        this.l  = -1;
        this.h = -1;
        this.w = -1;

    }

    Box(int l , int w , int h){
        this.l = l;
        this.w = w;
        this.h = h;
    }

    Box(Box other){
        this.l = other.l;
        this.w = other.w;
        this.h = other.h;
    }

}
