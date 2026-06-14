#include<bits/stdc++.h>
using namespace std;
int countDigit(int n) {
    int count = 0;
    if(n==0){
        return ++count;
    }
     int num =0;
    while(n>0){
       
        num = n%10;
        count++;
        n= n/10;
    }
    return count;
};
int main(){

    int value_count = countDigit(123999);
    cout<<"The count of digit is : "<<value_count<<endl;
    return 0;
}


     