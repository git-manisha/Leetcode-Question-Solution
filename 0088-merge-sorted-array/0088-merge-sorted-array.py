class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1)-1

        n = n-1
        m = m-1
        while(n>=0 and m>=0):
            if(nums2[n]>nums1[m]):
                nums1[i] = nums2[n]
                n =n-1
            else:
                nums1[i] = nums1[m]
                m =m-1
            i=i-1
        
        while(i>=0 and n>=0):
            nums1[i] = nums2[n]
            n -=1
            i -=1
        
        while(i>=0 and m>=0):
            nums1[i] = nums1[m]
            m -=1
            i -=1
        return nums1
        



        