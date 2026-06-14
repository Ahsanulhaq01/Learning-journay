#include<bits/stdc++.h>
using namespace std;
int main(){
  list<int>l = {1,2,3,4,5,6,7,8};
  queue<int>q;
  for(auto value : l){
    q.emplace(value);
  }

  while (!q.empty())
  {
    cout<<q.front()<<endl;
    q.pop();
  }
  
  return 0;
}