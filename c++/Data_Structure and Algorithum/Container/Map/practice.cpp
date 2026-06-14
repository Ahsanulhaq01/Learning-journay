#include<bits/stdc++.h>
using namespace std;
int main(){

  // map<int,int> m;
  // m.emplace(2,3);
  // m.emplace(4,3);
  // m.emplace(1,5);
  // m.emplace(3,9);

  // for(auto it : m){
  //   cout<<it.first<<"  :  "<<it.second<<endl;
  // }

  // map<int,pair<int,int>>mpp;
  // list<pair<int,int>>l ={ {1, {2}}, {1, {2}}, {1, {2}}, {1, {2}}, {1, {2}} };

  // mpp.insert({2,{3,2}});
  // for(auto value : l){
  //   mpp.insert({value.first, {value.second, 0}}); 
  // }

  // for(auto val : mpp){
  //   cout << val.first << " => (" << val.second.first << ", " << val.second.second << ")" << endl;
  // }

  unordered_map<int,int>mmp;

  mmp.emplace(3,2);
  mmp.emplace(1,2);
  mmp.emplace(2,2);
  mmp.emplace(5,2);
  mmp.emplace(3,2);

  for(auto each:mmp){
    cout<<each.first<<"  "<<each.second<<endl;
  }
  return 0;
}