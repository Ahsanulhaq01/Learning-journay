#include<bits/stdc++.h>
using namespace std;
int main(){
  //try fro set,mutliset and unordered set 
  unordered_set<int> s;
  list<int> l = {1,2,3,20,5,6,7,8,8,8,8,8};
  for(auto value : l){
    s.emplace(value);
  }

  for(auto print : s){
    cout<<print<<" ";
  }
  
  return 0;
}