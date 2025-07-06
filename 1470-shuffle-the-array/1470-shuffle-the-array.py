class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        itr = 0
        i=0
        res_list = [0]*len(nums)
        while(i<n):
            res_list[itr] = nums[i]
            res_list[itr+1] = nums[i+n]
            itr +=2
            i +=1
        
        return res_list
        