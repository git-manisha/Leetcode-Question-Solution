class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        if(nums.size()==1 && nums[0]==k){
            return 1;
        }
        unordered_map<int,int> mp;
        int count=0;
        int sum=0;
        mp.insert({0,1});
        for(int i=0;i<nums.size();i++){
            sum = sum+nums[i];
            if(mp.find(sum-k) != mp.end()){
                count += mp[sum-k];
            }
            mp[sum]++;
        }

        return count;
    }
};