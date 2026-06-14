#include<bits/stdc++.h>
using namespace std;
int main(){
  /*
  code to print the details of five student using pair container
  int rollNo;
  string name;
  cout<<"Enter the Data of five outstanding student ! \n";
  vector<pair<int,string>> v;

  for(int i = 0;i<5;i++){
    cin>>rollNo;
    cin>>name;
    v.emplace_back(rollNo,name);
  }
  cout<<"\t \tThe details of student as :"<<endl;
  for(int i = 0;i<v.size();i++){
    cout<<v[i].first<<"\t";
    cout<<v[i].second<<endl;

  }
*/

//incomplete question solution !
  vector<pair<int,int>>v = { {1, 5}, {3, 2}, {4, 1} };
  pair<int,int> temp ={0,0};
  vector<pair<int,int>>::iterator t = v.begin();
  for(int i = 0;i< v.size()-1; i++){
    if(v[i].second>v[i+1].second){
      temp = v[i];
      v[i] = v[i+1];
      v[i+1] = temp;
    
    }
    cout << "(" << t->first << ", " << t->second << ")" << endl;
    t++;

  }
  
  
  
  
  return 0;
}