class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        direction = []
        for i in range(len(nums) - 1):
            j = i + 1
            if (nums[i] > nums[j]):
                direction.append("decreasing")
            elif (nums[i] < nums[j]):
                direction.append("increasing")
            else:
                direction.append("equal")
        return all(dir == "increasing" or dir == "equal" for dir in direction) or all(dir == "decreasing" or dir == "equal" for dir in direction)

            