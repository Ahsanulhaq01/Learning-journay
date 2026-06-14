#include<bits/stdc++.h>
using namespace std;
void print(string s,int i){

  if(i<0)return;
  cout<<s[i];
   print(s,i-1);
   
}
int main(){
  print("ahsanulhaq",10);
  return 0;
}