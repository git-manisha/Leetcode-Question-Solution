class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        hashmap = {}
        hashmap[0] = 1
        i = 0
        preSum =0
        while(i<len(nums)):
            preSum +=nums[i]
            if(preSum-k in hashmap):
                result +=hashmap[preSum-k]
            if(preSum not in hashmap):
                hashmap[preSum] = 1
            else:
                hashmap[preSum] += 1
            i +=1
        
        return result