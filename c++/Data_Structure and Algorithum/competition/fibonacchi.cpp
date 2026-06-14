#include <bits/stdc++.h>
using namespace std;
void swap(int a, int b)
{
    a = a ^ b;
    b = a ^ b;
    a = a ^ b;

    cout << b << " " << a << endl;
}
void oddEven(int a){
    if(a&1)cout<<"odd";
    else 
    cout<<"even";
}
void powerOfTwo(int n){
    if(n > 0 && (n &(n-1)) ==0 ){
        cout<<"power of two"<<endl;
    }
    else{
        cout<<"not power of two";
    }
}
void coutnsetBit(int n ){
    int dup = n;
    int count =0;
    while(dup > 0){
        count += (dup & 1);
        dup >>= 1;
    }
    cout<<"no of setBit"<<count<<endl;
}
void freq(vector<int> arr){
    unordered_map<int,int>mp;
    for(int i = 0;i<arr.size();i++){
        mp[arr[i]] = 0;
    }
    for(int i =0;i < arr.size();i++){
        mp[arr[i]] +=1;
    }
    for(auto val : mp){
        cout<<val.first<<"      "<<val.second<<endl;
    }
}
void second(vector<int>arr){
    int fl = INT_MIN;
    int sl=INT_MIN;

    for(int i =0;i<arr.size();i++){
        if(arr[i] > fl){
            sl = fl;
            fl = arr[i];
        }
        else if(arr[i] > sl && arr[i] != fl){
            sl = arr[i];
        }
    }

    cout<<"second largest : "<<sl <<"           "<<"first Largest :"<<fl<<endl;
}
void sarr(vector<int>arr){
    sort(arr.begin(),arr.end());
    for(int val : arr){
        cout<<val<<"  ";
    }
    cout<<endl;
}
void fibo(int n){
    vector<int>a(n);
    a[0] = 0;
    a[1] = 1;

    for(int i = 2;i<n;i++){
        a[i] = a[i-1] + a[i-2];
    }
    for(auto val : a){
        cout<<val<<" ";
    }
    cout<<endl;
}
int fact(int n){
    if(n <= 1)return 1;
    return n * fact(n-1);
}
void prime(int n){
    if(n <=1){
        cout<<"not a prime";
        return;
    }

    for(int i=2;i <=sqrt(n);i++){
        if(n % i== 0){
            cout<<"not a prime No"<<endl;
            return;
        }
    }

    cout<<"prime No"<<endl;
}
void decensort(vector<int>arr){
    int n = arr.size();
    sort(arr.begin() , arr.end() );
    // reverse(arr.begin() , arr.end());
    for(int val : arr){
        cout<<val<<" ";
    }
    cout<<endl;
}

int main()
{
    // swap(4, 5);
    // prime(5);
    // powerOfTwo(8);
    // powerOfTwo(10);
    // coutnsetBit(7);

    decensort({11,2,2,3,3,3,34,2,4,2,5,5,5,5});
    // fibo(10);
    // long long val = prime(5);
    // prime(2);
    return 0;
}
