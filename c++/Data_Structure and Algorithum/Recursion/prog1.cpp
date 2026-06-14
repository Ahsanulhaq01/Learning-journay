#include<bits/stdc++.h>
using namespace std;
int mycount = 1;
void printNthTime(){
  if(mycount == 6){
    return;
  }
  else
  {
    cout<<"The count number is :" <<mycount<<endl;
    mycount++;
  printNthTime();
  }
}
int main(){
  
  printNthTime();
  return 0;
}