#include<bits/stdc++.h>
using namespace std;
int main(){
  /*
  creating of pair using constructor
  pair<int,string> p(43,"pakistan");
  cout<<p.first;
  cout<<endl;
  cout<<p.second<<"\n";

creating of pair using make_pair built-in function!
  auto p = make_pair("pakistan",45);
  cout<<"\n"<<p.first;
  cout<<"\n"<<p.second<<endl;

creating of pair using manual methond
  pair<double,double> flo = {43.2,43.2};
  cout<<flo.first + flo.second;

we can store pair in array ,vector ,map etc:
    */
   
  vector<pair<int,string>> v = {{3,"pakistan"},{4,"thailand"},{5,"USA"}};

    v.push_back({6,"afganistan"});
    v.emplace_back(7,"malaysia");
  for(int i =0;i<v.size();i++){

    cout<<v[i].first<<"\t";
    cout<<v[i].second<<endl;
  }


  return 0;
}