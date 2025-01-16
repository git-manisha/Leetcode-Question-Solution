class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap = {}
        hashmap[0] = -1
        i =0
        presum = 0
        while(i<len(nums)):
            presum +=nums[i]
            rem = presum%k
            if(rem in hashmap):
                if((i-hashmap[rem])>=2):
                    return True
            else:
                hashmap[rem] = i
            i +=1
        
        return False



        