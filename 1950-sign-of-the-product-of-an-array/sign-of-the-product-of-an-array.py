class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product = 1 
        for i in nums:
            product *= i
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0
        