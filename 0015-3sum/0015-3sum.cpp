class Solution {
public:
    vector<vector<int>> ans;
    void twoSum(int target,vector<int>& nums,int j,int k){
        while(j<k){
            if(nums[j]+nums[k] > target){
                k--;
            }
            else if(nums[j]+nums[k] < target){
                j++;
            }
            else{
               
            while(j<k && (nums[j] == nums[j+1])){ j++; }
            
            while(j<k && (nums[k] == nums[k-1])){ k--; }
            ans.push_back({-target,nums[j],nums[k]});
           
            j++;
            k--;
            }
        }
    }
    vector<vector<int>> threeSum(vector<int>& nums) {
        if(nums.size()<3){
            return {};
        }
        int n = nums.size();
        ans.clear();
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size()-2;i++){
            if(i>0 && (nums[i] == nums[i-1])){
                continue;
            }
            int n1 = nums[i];
            int target = -n1;
            twoSum(target,nums,i+1,n-1);
        }
        return ans;
    }
};