#include <stack>
class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {
        /* MY SOLUTION
        long long int minMumSum = 0;
        for (int i = 0;i<arr.size();i++){
            minMumSum+=arr[i];
            minMumSum=minMumSum%1000000007;
            int currentMinimum = arr[i];
            for(int j = i+1;j<arr.size();j++){
                if(currentMinimum>arr[j]){
                    currentMinimum=arr[j];
                }
                minMumSum+=currentMinimum;
                minMumSum=minMumSum%1000000007;
            }
        }
        return minMumSum;
        LEETCODE'S SOLUTION
        */
        int MOD = 1000000007; // module for the return value
        stack<int> stack;// monotonic stack
        long int sumOfMinimums = 0;
        for(int i = 0; i<=arr.size();i++){ // for every element in the array
            while(!stack.empty() && (i == arr.size()|| arr[stack.top()]>=arr[i])){
                // if the stack is not empty and we're not at the end of the array
                // or the top element of the array is greater or equal than the current item
                int mid = stack.top();stack.pop(); // item that we'll pop
                int leftBoundary = stack.empty() ? -1 : stack.top(); // if empty -1 if not then the top of the stack
                int rightBoundary = i; // our current element
                long int count = (mid - leftBoundary) * (rightBoundary - mid) % MOD; // count of subarrays
                                                                                    //where the element to extract is the lowest
                sumOfMinimums +=(count*arr[mid])%MOD;
                sumOfMinimums %=MOD;
            }
            stack.push(i);
        }
        return sumOfMinimums;
    }
};