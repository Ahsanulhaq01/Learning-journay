#include<bits/stdc++.h>
using namespace std;
// int main(){
//   stack<int>ahsan;
//   ahsan.emplace(3);
//   ahsan.emplace(4);
//   for(int i = 10;i<155;i++){
//     ahsan.emplace(i);
//   }
//   cout<<ahsan.top();
//   cout<<endl;
//   cout<<ahsan.empty();
//   for(auto s : ahsan){
//     cout<<s<<endl;
//   }
//   return 0;
// }

int main() {
  stack<int> ahsan;
  ahsan.emplace(3);
  ahsan.emplace(4);
  
  for(int i = 10; i < 15; i++) {
      ahsan.emplace(i);
  }

  // Safely print top (if stack is not empty)
  if(!ahsan.empty()) {
      cout << ahsan.top() <<"Pakistan is our country"<< endl;
  }

  // Print all elements by popping (destructive)
  while(!ahsan.empty()) {
      cout << ahsan.top() << endl;
      ahsan.pop(); // Remove the top element
  }

  return 0;
}