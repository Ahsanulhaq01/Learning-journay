#include<iostream>
using namespace std;
void print(int n){
  int num = 1;
  for(int i = 0;i<n;i++){
    for(int j = 1 ;j<=i +1;j++ ){
      cout<<num++<<" ";
    }
    cout<<endl;
  }

}
int main(){
  print(5);

  return 0;
}