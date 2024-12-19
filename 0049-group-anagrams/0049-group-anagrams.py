class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mydict = {}
        for word in strs:
            temp =''.join(sorted(word))
            if(temp not in mydict):
                mydict[temp] = [word]
            else:
                mydict[temp].append(word)
        
        ans = []
        for val in mydict.values():
            ans.append(val)
        
        return ans
        