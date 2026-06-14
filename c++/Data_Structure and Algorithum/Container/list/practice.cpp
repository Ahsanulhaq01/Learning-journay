#include<bits/stdc++.h>
using namespace std;
int main(){
  list<int> l = {1,2,3,4,5,6};
  list<int> l2 = {7,8,9,10};

  l.insert(l.end(),l2.begin(),l2.end());
  l.insert(l.end(),100);
  cout<<l.front()<<endl;
  for(auto value : l){
    cout<<value<<endl;
  }
  return 0;
}