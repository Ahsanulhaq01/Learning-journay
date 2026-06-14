#include<bits/stdc++.h>
using namespace std;
int print(int value){
  if(value < 1)return 0;
  else{
    return value + print(value-1);
  }
}
int main(){
  int sum = print(5);
  cout<<"The sum of nth Number is : "<<sum<<endl;
  return 0;
}