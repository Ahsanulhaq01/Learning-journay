#include<bits/stdc++.h>
using namespace std;
bool isPrime(int x){
  int count =0;
  for(int i= 1; i<=x; i++){//not optimized but will try our best to make it optimized 
    if(x % i == 0){
      count++;
    }
  }
  if(count==2)
    return true;
  else 
    return false;
}
int main()
{
  cout<<"\t"<<isPrime(4)<<"\t";
 return 0; 
}
