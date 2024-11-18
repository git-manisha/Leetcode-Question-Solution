class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        for(int i:nums){
            mp[i]++;
        }
        vector<vector<int>> v(nums.size()+1);
        for(auto &it:mp){
            int value = it.first;
            int freq = it.second;

            v[freq].push_back(value);
        }
        int n = v.size()-1;
        vector<int> result;
        for(int i=n;i>=0;i--){
            if(v[i].size() == 0){
                continue;
            }
            while(v[i].size()>0 && k>0){
                result.push_back(v[i].back());
                v[i].pop_back();
                k--;
            }
        }
        return result;
    }
};