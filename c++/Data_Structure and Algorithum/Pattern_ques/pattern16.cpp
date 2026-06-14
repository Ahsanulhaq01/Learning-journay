#include<bits/stdc++.h>
using namespace std;
void print(int n){

  for (int i = 0; i < n; i++)
  {
    //for spaces 
    for(int j = 0;j<n-i-1;j++){
      cout<<" ";
    }
    //for character
    for(char k ='A'; k<='A'+i;k++){
      cout<<k;
    }
    //for printing char inversly 
    for(char l= 'A'+i-1;l >='A'+ 0;l--){
      cout<<l;
    }
    cout<<endl;
  }
  
}
int main(){
  print(4);
  return 0;
}