class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if(len(s1)>len(s2)):
            return False
        arr = [0]*26
        arr1 = [0]*26
        i=0
        while(i<len(s1)):
            idx = ord(s1[i])-ord('a')
            arr[idx] +=1
            i +=1

        n = len(s1)
        i=0
        j=0
        while(j<len(s2)):
            if((j-i+1)<n):
                idx = ord(s2[j])-ord('a')
                arr1[idx] +=1
            else:
                idx = ord(s2[j])-ord('a')
                arr1[idx] +=1
                if(arr ==arr1):
                    return True
                idx = ord(s2[i])-ord('a')
                arr1[idx] -=1
                i +=1
            j +=1
        
        return False
        

        