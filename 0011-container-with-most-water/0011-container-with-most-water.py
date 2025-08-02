class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        first = 0
        last = len(height)-1
        while(first<last):
            if(height[first]<height[last]):
                height[first] = (last-first)*height[first]
                first +=1
            else:
                height[last] = (last-first)*height[last]
                last -=1
            
        return max(height)
                
        