class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        while(k>0):
            temp = nums.pop()
            nums.insert(0,temp)
            k -=1
        