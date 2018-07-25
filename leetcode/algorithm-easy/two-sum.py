class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        vals=dict()
        i=0
        while i < len(nums):
            vals[nums[i]]=i
            i+=1
        i=0
        while i < len(nums):
            key = target-nums[i]
            if (key in vals and vals[key]!=i):
                return [i,vals[key]]
            i+=1
