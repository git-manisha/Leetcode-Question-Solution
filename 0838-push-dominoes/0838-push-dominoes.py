class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        ans = ""
        right_list = [0]*len(dominoes)
        left_list = [0]*len(dominoes)
        prev = "."
        count =1
        i=0
        while(i<len(dominoes)):
            if(dominoes[i]=='R'):
                prev = 'R'
                count = 1
            elif(dominoes[i]=='L'):
                prev = 'L'
            if(prev =='R' and dominoes[i]=='.'):
                right_list[i] = count
                count +=1
            i +=1
        prev = "."
        count =1
        i = len(dominoes)-1
        while(i>=0):
            if(dominoes[i]=='L'):
                prev = 'L'
                count=1
            elif(dominoes[i]=='R'):
                prev = 'R'
            if(prev =='L' and dominoes[i]=='.'):
                left_list[i] = count
                count +=1
            i -=1
        i=0
        while(i<len(dominoes)):
            if(left_list[i]==0 and right_list[i]==0):
                ans +=dominoes[i]
            elif(right_list[i]==0):
                ans +='L'
            elif(left_list[i]==0):
                ans +='R'
            elif(left_list[i]>right_list[i]):
                ans +='R'
            elif(left_list[i]<right_list[i]):
                ans +='L'
            else:
                ans +=dominoes[i]
            i +=1
        
        return ans