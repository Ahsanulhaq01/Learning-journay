#include<bits/stdc++.h>
using namespace std;
void allDivisor(int x){
  vector<int> d;
  for(int i = 1;i<=x;i++){//brute force not an optimize code 
    if(x%i==0){
      d.push_back(i);
    }
    
  }
  for(auto i : d){
    cout<<" "<<i;
  }
  cout<<endl;

}
int main()
{
  allDivisor(36);
  return 0;
}
