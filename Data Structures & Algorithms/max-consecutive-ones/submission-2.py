class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_counter = 0
        counter = 0
        for i in range(len(nums)):
            if nums[i] != 1:
                max_counter = max(max_counter, counter)
                counter = 0
            else:
                counter += 1
        return max(max_counter, counter)

