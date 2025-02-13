class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if(k==1):
            return 0
        nums.sort()
        i=k-1
        j=0
        mini = 100000
        while(i<len(nums)):
            mini = min((nums[i]-nums[j]),mini)
            i +=1
            j +=1
        
        return mini