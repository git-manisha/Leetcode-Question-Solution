class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a)-1
        j = len(b)-1
        result = ""
        c =0
        while(i>=0 and j>=0):
            s = (int(a[i])+int(b[j])+c)%2
            c = (int(a[i])+int(b[j])+c)/2
            result = str(s)+result
            i -=1
            j -=1
        while(i>=0):
            s = (int(a[i])+c)%2
            c = (int(a[i])+c)/2
            result = str(s)+result
            i -=1
        while(j>=0):
            s = (int(b[j])+c)%2
            c = (int(b[j])+c)/2
            result = str(s)+result
            j -=1
        
        if(c!=0):
            result = str(c)+result
        
        return result
