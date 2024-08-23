class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int product = 1;
        int count =0; 
        int pos;
        for(int i =0;i<nums.size();i++){
            if(nums[i] !=0){
                product = product*nums[i];
            }
            else{
                count++;
                pos = i;
            }
        }
        vector<int> ans(nums.size(),0);
        if(count > 1){
            return ans;
        }
        else if(count == 1){
            ans[pos] = product;
        }
        else{
        for(int i=0;i<nums.size();i++){
                ans[i]=product/nums[i]; 
        }
        }
        return ans;
    }
};