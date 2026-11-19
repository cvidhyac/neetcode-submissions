class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isIncreasing = True
        isDecreasing = True

        if not nums:
            return False
            
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                isDecreasing = False
            if nums[i] > nums[i + 1]:
                isIncreasing = False

        return isIncreasing or isDecreasing