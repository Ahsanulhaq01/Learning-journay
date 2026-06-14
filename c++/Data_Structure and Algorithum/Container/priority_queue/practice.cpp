#include<bits/stdc++.h>
using namespace std;
int main(){
    /*
  list<int> l = { 1,2,3,4,5,6,7,8,9,10};

  priority_queue<int> pq;

  for(auto value : l){
    pq.push(value);
  }

  while (!pq.empty())
  {
    cout<<pq.top()<<endl;
    pq.pop();
  }
    */
  //for string 
  // priority_queue<string,vector<string>,greater<string>> min_heap;
  priority_queue<string>min_heap;

  list<string> name = {"z","b","c","d","a"};

  //code to for integer things
  // list<int> l = {1,2,3,4,5,6,7,8,9,10};

  // priority_queue<int,vector<int>,greater<int>> min_heap;
  for(auto value:name){
    min_heap.emplace(value);
  }

  while (!min_heap.empty())
  {
    cout<<min_heap.top()<<endl;
    min_heap.pop();
  }
  
  return 0;

}