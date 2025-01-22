class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        queue = []
        i=1
        while(i<=8):
            queue.append(i)
            i +=1
        
        ans = []
        
        for num in queue:
            if(num>low and num<high):
                ans.append(num)
            rem = num%10
            if(rem+1 <=9):
                queue.append((num*10)+rem+1)
            if(num >high):
                break
        
        return ans
            



        