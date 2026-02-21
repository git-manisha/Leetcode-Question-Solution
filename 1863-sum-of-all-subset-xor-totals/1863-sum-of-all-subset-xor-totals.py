class Solution(object):
    total = 0
    def rec(self,i,xor,nums,n):
        if(i==n):
            self.total +=xor
            return 
        
        self.rec(i+1,xor,nums,n)

        self.rec(i+1,xor^nums[i],nums,n)

    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        self.total = 0
        n = len(nums)
        xor = 0

        self.rec(0,xor,nums,n)

        return self.total