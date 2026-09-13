#include <bits/stdc++.h>
using namespace std;
vector<int> twoSum(vector<int> &arr  , int target)
{
    int n = arr.size();
    unordered_map<int , int> ump;
    for (int i = 0; i < n; i++)
    {
        int val = target - arr[i];

        auto findInMap = ump.find(val);
        if(findInMap != ump.end()){
            return {findInMap->second , i};
        }

        ump[arr[i]] = i;

    }

    return {-1  , -1};
}
int main()
{
    vector<int> arr = {7, 2, 9, 11};
    int target = 9;
    vector<int> ans = twoSum(arr , target);

    //for verification 

    for(auto value : ans){
        cout<<value<<" ";
    }
    cout<<endl;
    return 0;
}

