class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_value = 0
        for i in candies:
            if(i>max_value):
                max_value = i

        i = 0
        while(i<len(candies)):
            temp = candies[i]+extraCandies
            if(temp >= max_value):
                candies[i] = True
            else:
                candies[i] = False
            i+=1
        return candies      