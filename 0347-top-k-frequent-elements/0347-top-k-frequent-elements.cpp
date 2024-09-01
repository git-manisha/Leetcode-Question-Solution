class Solution {
public:
    typedef pair<int,int> p;
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        for(auto it:nums){
            mp[it]++;
        }

        vector<vector<int>> temp(nums.size()+1);
        for(auto it:mp){
            temp[it.second].push_back(it.first);
        }
        int n = nums.size();
        vector<int> result;
        for(int i=n;i>=0;i--){
            if(temp[i].size()==0){
                continue;
            }
            while(temp[i].size()>0 && k>0){
                result.push_back(temp[i].back());
                temp[i].pop_back();
                k--;
            }
        }
        return result;
    }
};