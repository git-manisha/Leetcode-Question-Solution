class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        presum = 0
        l1 = []
        for itr in nums:
            presum +=itr
            l1.append(presum)

        i=0
        sum1 =0
        s = len(nums)-1
        while(i<len(nums)):
            nums[i] = ((nums[i]*i)-(l1[i]-nums[i]))+((l1[s]-l1[i])-(nums[i]*(len(nums)-i-1)))
            i +=1
        
        return nums


            

