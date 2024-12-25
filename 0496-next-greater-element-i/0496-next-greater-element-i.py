class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map1 = {}
        i=0
        while(i<len(nums2)):
            j=i+1
            if(nums2[i] not in map1):
                while(j<len(nums2)):
                    if(nums2[i]<nums2[j]):
                        map1[nums2[i]] = nums2[j]
                        break
                    j +=1
            i +=1
        res = []
        for i in nums1:
            if(i in map1):
                res.append(map1[i])
            else:
                res.append(-1)
        return res


        