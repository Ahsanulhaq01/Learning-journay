#include<bits/stdc++.h>
using namespace std;
void print(int value,int n){
  if(value > n)return;
  else{
        
    print(value+1,n);
    cout<<"The value is : "<<value<<endl;
  }
}
int main(){
  print(1,5);
  return 0;
}