#include<iostream>
using namespace std;
void print(int n){

  for(int i = 0 ;i < n;i++){
    for(int j =1;j<=i+1;j++){
      cout<<j;
    }
    for(int k = 1;k < n-i;k++){
      cout<<"  ";
    }
    for(int j = i+1; j>0; j--){
      cout<<j;
    }
    cout<<endl;
  }
}
int main(){
  print(4);
  return 0;
}