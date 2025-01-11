class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashmap = {}
        presum = 0
        hashmap[presum] = 1
        i=0
        count = 0
        while(i<len(nums)):
            presum +=nums[i]
            temp = presum-k
            if(temp in hashmap):
                count +=hashmap[temp]
            if(presum not in hashmap):
                hashmap[presum] = 1
            else:
                hashmap[presum] +=1
            i +=1
        return count

