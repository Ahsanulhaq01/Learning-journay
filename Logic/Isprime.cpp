#include<bits/stdc++.h>
using namespace std;
void Isprime(int n){
  int count = 0;
  for(int i = 1;i<=n;i++){
    if(n%i==0)
    count++;
  }
  if(count>2){
    cout<<"Not a prime number :"<<n<<endl;
    exit;
  }
  else if(count==2){
    cout<<"Prime no "<<n<<endl;
  }

}
int main(){

  for(int i= 0;i<100;i++){
    Isprime(i);
  }

  return 0;
}