#include<bits/stdc++.h>
using namespace std;
void elfreq(int arr[],int size,int lar){
  int hashh[lar] = {0};
  for(int i = 0;i<size;i++){
    hashh[arr[i]]++;
  }
  
  int q;
  int number;
  cin>>q;
  while (q--)
  {
    cin>>number;
    cout<<hashh[number]<<"\t"<<endl;
   
  }
  
  // int high = 0;
  // int low = 0;
  // for(int i= 0 ; i< lar;i++){
  //   if(hashh[i] > hashh[i+1]){
  //     low = hashh[i+1];
  //     high = hashh[i];
  //   }
  // }
  // cout<<high<<"\t"<<endl;
  // cout<<low<<"\t"<<endl;

}
int main(){
  int arr[] = {1,2,2,3,3,4,5,5};
  elfreq(arr,8,6);
  return 0;
}