class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap = {}

        i=0
        while(i<len(nums)):
            if(nums[i] in hashmap):
                diff = i-hashmap[nums[i]]
                hashmap.pop(nums[i])
                if(diff <= k):
                    return True
            hashmap[nums[i]] = i
            i +=1
        

        return False
        