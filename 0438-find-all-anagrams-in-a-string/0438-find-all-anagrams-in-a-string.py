class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if(len(p)>len(s)):
            return []
        l1 = [0]*26
        for ch in p:
            i = ord(ch)-ord('a')
            l1[i] = l1[i]+1
        
        l2 = [0]*26
        i=0
        j=0
        ans = []
        while(j<len(p)-1):
            idx = ord(s[j])-ord('a')
            l2[idx] +=1
            j +=1
        
        while(j<len(s)):
            idx = ord(s[j])-ord('a')
            l2[idx] +=1
            if(l1 == l2):
                ans.append(i)
            idx1 = ord(s[i])-ord('a')
            l2[idx1] -=1
            i +=1
            j +=1
        return ans

        