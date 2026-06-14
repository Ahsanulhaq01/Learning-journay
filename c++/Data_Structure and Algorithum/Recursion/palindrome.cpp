#include<bits/stdc++.h>
using namespace std;
bool IsPalindrome(int i, string &s){

  if(i >= s.size()/2)return true;
  if(s[i] != s[s.size() - i - 1])return false;
  return  IsPalindrome(i+1,s);
}
int main(){
  string s = "MAsAM";
  cout<<IsPalindrome(0,s)<<endl;
  return 0;
}

//extra things to be learn 
// int main(){
//   string a = {"abcdef"};
//   string b = "      ";
//   transform(a.begin(),a.end(),b.begin(),::toupper);

//   for(char value : b){
//     cout<<value<<endl;
//   }
//   return 0;
// }




