class Solution(object):
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """
        comp = ""
        i=0
        
        while(i<len(word)):
            count = 0
            ch = word[i]

            while(i<len(word) and count<9 and word[i]==ch):
                count +=1
                i +=1
            comp += str(count)+ch
        

        return comp