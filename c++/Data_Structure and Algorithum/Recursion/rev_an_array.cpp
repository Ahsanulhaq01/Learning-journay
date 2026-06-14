#include<bits/stdc++.h>
using namespace std;
void print(int arr[],int size){
  //using for loop 
  // for(int i = 1;i<= size;i++){
  //   cout<<arr[size - i];
  // }


  //using recursive function 
  if(size == 0)return;
  else{
    cout<<arr[size-1]<<" ";
  print(arr,size-1);
  }

  
}
int main(){
  int arr[] = {2,32,3,43,5,6,75,4,3,2};
  int size = sizeof(arr)/sizeof(0);
  
  print(arr,size);
  return 0;
}