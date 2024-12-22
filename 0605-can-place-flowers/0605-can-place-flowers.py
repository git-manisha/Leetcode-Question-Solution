class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if(len(flowerbed)==1 and flowerbed[0]==0):
            return True
        i=0
        while(i<len(flowerbed) and n!=0):
            if flowerbed[i]==0:
                if((i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0)):
                    flowerbed[i] = 1
                    n = n-1    
            i = i+1

        if n==0:
            return True
        return False
            
            

        