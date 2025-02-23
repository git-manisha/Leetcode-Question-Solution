class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        i=0
        j=0
        total = 0
        res =0
        while(j<len(arr)):
            if((j-i+1)<k):
                total +=arr[j]
            else:
                total +=arr[j]
                if(total/k >=threshold):
                    res +=1
                total -=arr[i]
                i +=1
            j +=1
        
        return res


        