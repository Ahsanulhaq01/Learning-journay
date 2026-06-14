#include<iostream>
using namespace std;
bool checkArmStrong(int x){
  int digit = 0;
  int dup  = x;
  int sum = 0;
  while (x != 0)
  {
    digit = x % 10;
    x = x / 10;
    sum += (digit * digit *digit) ;
  }
  return sum == dup;
  

}
int main(){
  cout<<checkArmStrong(212)<<endl;
  return 0;
}