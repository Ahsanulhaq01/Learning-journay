#include<iostream>
using namespace std;
void print(int n){

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
    int n ;
    cout<<"Enter the number of your consent :";
    cin>>n;
    print(n);
    return 0;
}