class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        list1 = set()
        for i in nums:
            if i in list1:
                return True
            else:
                list1.add(i)
        return False
        