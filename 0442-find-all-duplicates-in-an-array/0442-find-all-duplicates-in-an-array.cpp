class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        unordered_map<int,int> mp;
        for(auto it:nums){
            mp[it]++;
        }
        vector<int> result;
        for(auto itr:mp){
            if(itr.second >=2){
                result.push_back(itr.first);
            }
        }
        return result;
    }

};