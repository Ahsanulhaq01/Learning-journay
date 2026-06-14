#include<iostream>
#include<string>
using namespace std;
bool IsPalindrom(string s){
  string revstring = "";
  for(int i = s.length();i>=0;i--){
    revstring.push_back(s[i]);
  }
  cout<<revstring<<endl;

  if(s==revstring){
    return true;
  }
  else
  return false;
}
int main(){
  bool value = IsPalindrom("madam");
  cout<<value<<endl;
  return 0;
}