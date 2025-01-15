def to_swap(num1,num2):
    if(int(str(num2)+str(num1)) < int(str(num1)+str(num2))):
        return True
    return False
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        l1 = []
        l1.append(nums[0])
        i=1
        while(i<len(nums)):
            l1.append(nums[i])
            j = len(l1)-1
            while(j>0):
                if(to_swap(l1[j],l1[j-1])):
                    l1[j],l1[j-1] = l1[j-1],l1[j]
                j -=1
            i +=1
        
        ans = ""
        for ch in l1:
            ans +=str(ch)
        if(int(ans) == 0):
            return '0'
        return ans

        