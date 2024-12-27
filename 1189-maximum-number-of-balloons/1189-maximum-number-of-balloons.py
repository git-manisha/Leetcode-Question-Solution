class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        hashmap = {}
        hashmap['b'] =0
        hashmap['a'] =0
        hashmap['l'] =0
        hashmap['o'] =0
        hashmap['n'] =0
        i =0
        while(i<len(text)):
            if(text[i]=='b' or text[i]=='a' or text[i]=='l' or text[i]=='o' or text[i]=='n'):
                    hashmap[text[i]] += 1
            i +=1
        
        x = min(hashmap['b'],hashmap['a'],hashmap['n'])
        y = min(hashmap['l'],hashmap['o'])

        return min(y/2,x)