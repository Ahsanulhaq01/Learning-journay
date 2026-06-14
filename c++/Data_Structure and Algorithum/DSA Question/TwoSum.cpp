#include<bits/stdc++.h>
using namespace std;
// vector<int> twoSum(vector<int>& nums, int target) {
//   vector<int> index ;
//   for(int i = 0;i<nums.size();i++){

//       for(int j = 0; j < nums.size() ;j++ ){
//           if(nums[i] + nums[j+1] == target){
//             if(i==j+1){
//               continue;
//             }
//               index.push_back(i);
//               index.push_back(j+1);
//               break;
//           }
          
//       }
//       if(index.size()>0){
//         break;
//       }
//   }
//   return index;
// }

//Right and submitted answer ! 
vector<int> twoSum(vector<int>& nums, int target) {
  vector<int> index ;
  for(int i = 0;i<nums.size();i++){

      for(int j = 1; j < nums.size() ;j++ ){
          if(nums[i] + nums[j] == target){
            if(i==j){
              continue;
            }
              index.push_back(i);
              index.push_back(j);
              break;
          }
          
      }
      if(index.size()>0){
        break;
      }
  }
  return index;
}
int main(){

  vector<int> a = {2,5,5,11};
  int target = 10;
  vector<int> value = twoSum(a,target);
  for(auto i : value){
    cout<<i<<" ";
  }
  
  return 0;
}


// vector<int> twoSum(vector<int>& nums, int target) {
//   vector<int> index ;
//   for(int i = 0;i<nums.size();i++){

//       for(int j = 1; j < nums.size() ;j++ ){
//           if(nums[i] + nums[j] == target){
//               index.push_back(i);
//               index.push_back(j);
//               break;
//           }
          
//       }
//       if(index.size()>0){
//         break;
//       }
//   }
//   return index;
// }