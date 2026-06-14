#include<bits/stdc++.h>
using namespace std;
int main(){
  vector<int> v = {1,2,3,4,5,65,6};
 int a[] = {1,3,4,5,6,79};
  int max = *max_element(a,a+6);
  cout<<max<<endl<<"Khan is for pakistan";
  /*
  code to traverse on vector 


  //printing through iterator
  // for(vector<int> ::iterator t = v.begin();t < v.end();t++){
  //   cout<<*t<<endl;
  // }
  //2nd way of iterating through loop
  // for(auto t = v.begin();t < v.end();t++){
  //   cout<<*t<<endl;
  // }

  //3rd shorts syntax to print it 

  // for(auto t : v){
  //   cout<<t<<endl;
  // }
  */
 /*
    code to delete/Insert and other method something from vector ! 

    v.erase(v.begin() + 1,v.begin()+4);

    v.insert(v.begin(),3,100);

    vector<int> v1(2,100);
      v.insert(v.begin(),v1.begin(),v1.end());
      v.pop_back();
      cout<<"Before Swaping "<<endl;
    for(auto t:v){
      cout<<t<<endl;
    }
    v.clear();
    bool vwal = v.empty();
    cout<<vwal<<"\tvwal  variabl value " <<endl;
    v1.clear();
    bool first = v1.empty();
    cout<<first<<"\tv1 first variabl value " <<endl;
    cout<<"After first !"<<endl;
    for(auto t:v1){
      cout<<t<<endl;
    }

    cout<<"hi i am ahsan"<<endl;
    cout<<"After Swaping "<<endl;
    v.swap(v1);
    for(auto t:v){
      cout<<t<<endl;
    }
    cout<<"After first !"<<endl;
    for(auto t:v1){
      cout<<t<<endl;
    }

    
 */


  return 0;
}