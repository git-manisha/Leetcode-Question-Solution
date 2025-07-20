class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        mini = 1
        maxi = max(piles)
        mini_banana = max(piles)
        while(mini < maxi):
            mid = mini + (maxi-mini)//2
            hour = 0
            i = 0
            while(i<len(piles)):
                if(piles[i]%mid == 0):
                    hour += piles[i]/mid
                else:
                    hour += (piles[i]/mid) +1
                i +=1
            if(hour <= h):
                maxi = mid
                mini_banana = mid
            else:
                mini = mid+1
        
        return mini_banana


