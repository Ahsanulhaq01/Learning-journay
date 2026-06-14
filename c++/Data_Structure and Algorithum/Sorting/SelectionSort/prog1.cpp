#include<bits/stdc++.h>
using namespace std;
void selectionSort(int arr[],int size){
  int min ;
  for(int i = 0;i < size-1 ;i++){
    min = i;
    for(int j = i+1 ; j<size;j++){
      if(arr[j] < arr[min])min = j;

    }
    swap(arr[min],arr[i]);
  }
}
int main(){
  int n;
  cin>>n;
  int arr[n] = {55,66,11,11,2,5,4,6,17};
  
  selectionSort(arr,n);
  for(int val : arr){
    cout<<val<<" ";
  }
  return 0;
}