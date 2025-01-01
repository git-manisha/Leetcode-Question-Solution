def swap(nums,j,k):
    temp = nums[j]
    nums[j] = nums[k]
    nums[k] = temp
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        k = len(nums)-1

        while(i<k and j<=k and i<=j):
            if(nums[j] == 2):
                swap(nums,j,k)
                k -=1
            elif(nums[j]==0):
                swap(nums,j,i)
                j +=1
                i +=1
            else:
                j +=1