class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        unordered_map<int,int> mp;

        for(int i=0;i<nums.size();i++){
            int remain = target-nums[i];
            if(mp.find(remain) != mp.end()){
                ans.push_back(mp[remain]);
                ans.push_back(i);
                break;
            }
            mp[nums[i]] = i;
        }

        return ans;
    }
};