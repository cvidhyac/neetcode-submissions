class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cons = []
        counter = 0
        for i in range(len(nums)):
            if nums[i] != 1:
                max_cons.append(counter)
                counter = 0
            else:
                counter += 1
        max_cons.append(counter)
        return max(max_cons)

