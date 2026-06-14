#include<bits/stdc++.h>
using namespace std;
void print(int n){
  for(int i = 1;i<=n;i++){
    for(char j ='A' + (n -i);j <'A'+ n;j++){
      cout<<j<<" ";
    }
    cout<<endl;
  }
}
int main(){
  print(5);
  return 0;
}