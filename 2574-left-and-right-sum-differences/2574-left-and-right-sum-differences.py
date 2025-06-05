class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        leftSum = [0]*n
        rightSum = [0]*n

        i = 0
        j = n-1
        while(i<n-1 and j>0):
            leftSum[i+1] = leftSum[i]+nums[i]
            rightSum[j-1] = rightSum[j]+nums[j]
            i +=1
            j -=1
        
        answer = []
        i = 0
        while(i<n):
            answer.append(abs(leftSum[i]-rightSum[i]))
            i +=1
        
        return answer

        

        