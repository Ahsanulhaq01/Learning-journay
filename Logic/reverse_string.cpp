#include<bits/stdc++.h>
using namespace std;
void reverseString(string n){
  int length = n.length()-1;
  for(int i = 0 ;i<=length;i++){
    cout<<n[length-i];
  }

}
int main(){
  reverseString("AHSAN");
  return 0;
}