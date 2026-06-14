#include<bits/stdc++.h>
using namespace std;
vector<int> bubbleSort(vector<int> &arr){
  int n = arr.size();
  
  for(int i=0 ;i < n-1;i++){
    bool swapped = 0;
    for(int j = 0; j < n-i-1;j++){
      if(arr[j]>arr[j+1]){
        swap(arr[j],arr[j+1]);
        swapped = 1;
      }
    }
    if(!swapped){
      break;
    }
   
  }
  return arr;
}
int main(){
  vector<int>arr = {1,2,3,4,5};
  vector<int> a = bubbleSort(arr);
  for(auto value : a){
    cout<<value<<" ";
  }
  return 0;
}