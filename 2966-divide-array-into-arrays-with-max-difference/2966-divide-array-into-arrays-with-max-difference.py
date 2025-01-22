class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        if(len(nums)<3):
            return ans
        nums.sort()
        i=2
        j = 0
        while(i<len(nums)):
            temp =[]
            if((nums[i]-nums[j]) <= k):
                ans.append([nums[itr] for itr in range(j,i+1)])
                j = i+1
                i +=3
            else:
                return []
        
        return ans

        