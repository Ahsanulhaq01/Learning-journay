#include<iostream>
using namespace std;
void print2(int n){

    for(int i = 0;i<n;i++){
        for(int k =0;k<i;k++){
            cout<<" ";
        }
        for(int j = 1;j<n+(n-(i+i));j++){
            cout<<"*";

        }
        for(int k =0;k<i;k++){
            cout<<" ";
        }
        cout<<endl;
    }
}
void print1(int n){

    for(int i = 0;i<n;i++){

        for(int k =1;k<n-i;k++){
            cout<<" ";
        }
        for(int j = 1;j<=i+i+1;j++){
            cout<<"*";
        }
        for(int k = 1;k<n-i;k++){
            cout<<" ";
        }
        cout<<endl;
    }
}
int main(){
    int n;
    cout<<"Enter the value of your consent";
    cin>>n;
    print1(n);
    print2(n);
    return 0;
}