#include<iostream>
using namespace std;
void print(int n){
    int start = 0;
    for(int i = 1;i <=(n*2)-1;i++){
        start = i;
        if(i>n) start = 2*n -i;
        for(int j =0;j<start;j++){
            cout<<"*";
        }
        
        cout<<endl;
    }
}
int main(){
    print(9);
    return 0;
}