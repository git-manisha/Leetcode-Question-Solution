class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hset = set()
        for x in nums:
            if x in hset:
                return True
            else:
                hset.add(x)
        
        return False
        