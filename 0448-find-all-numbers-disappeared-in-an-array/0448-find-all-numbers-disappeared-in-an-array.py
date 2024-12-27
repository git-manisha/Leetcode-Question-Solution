class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = nums[:]
        for i in nums:
            temp = i-1
            if(res[temp]>0):
                res[temp] = -(res[temp])
        
        answer = []
        itr=0
        while(itr<len(res)):
            if(res[itr] >0):
                answer.append(itr+1)
            itr +=1
        
        return answer
