class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str1 = ""
        for i in digits:
            str1 +=str(i)
        
        num = int(str1)+1
        str1 = str(num)
        res = []
        i=0
        while(i<len(str1)):
            res.append(int(str1[i]))
            i +=1

        return res

        