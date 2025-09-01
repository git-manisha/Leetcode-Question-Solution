class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.newArr = []
        self.newArr.append(nums[0])
        i = 1
        while(i<len(nums)):
            self.newArr.append(self.newArr[i-1]+nums[i])
            i +=1
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.newArr[right]
        else:
            return self.newArr[right]-self.newArr[left-1]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)