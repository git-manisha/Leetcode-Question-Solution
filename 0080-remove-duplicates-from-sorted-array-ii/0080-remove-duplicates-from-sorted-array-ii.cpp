class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
        for(int i=2;i<nums.size();i++)
        {
            if(nums[i]==nums[i-1])
            {
                if(nums[i-2]==nums[i-1])
                {
                    nums.erase(nums.begin()+i);
                    i--;
                }
            }
        }
        return nums.size();
    }
};