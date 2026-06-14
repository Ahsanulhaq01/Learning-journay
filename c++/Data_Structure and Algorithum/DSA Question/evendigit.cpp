#include<bits/stdc++.h>
using namespace std;
int findNumbers(vector<int>& nums) {
  string value = "";
  int counter = 0;
  for(int i= 0;i<nums.size();i++){
      string value = to_string(nums[i]);
      if(value.length()%2==0){
        counter++;
      }
  }
  return counter;
}
int main(){
  vector<int> a = {555,901,482,1771};
  int value = findNumbers(a);
  cout<<"the even digit are : "<<value<<endl;
  return 0;
}