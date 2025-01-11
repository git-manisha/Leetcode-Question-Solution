class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit =0
        i = 1
        while(i<len(prices)):
            if(prices[i-1]<prices[i]):
                indx = i-1
                while(i+1<len(prices) and prices[i]<=prices[i+1]):
                    i +=1
                max_profit = max_profit+(prices[i]-prices[indx])
            i +=1
        return max_profit

        