class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int maxsize=-1;
        for(int i=arr.size()-1;i>=0;i--)
        {
            int current =arr[i];
            arr[i]=maxsize;
            maxsize=max(maxsize,current);
        }
        return arr;
    }
};