#include<bits/stdc++.h>
using namespace std;
int main(){
  deque<int> d;
  d.push_back(300);
  d.emplace_back(100);
  d.insert(d.begin(),4,100);
  d.pop_back();
  d.push_back(500);
  d.erase(d.end());
  for(auto i : d){
    cout<<i<<endl;
  }
  return 0;
}