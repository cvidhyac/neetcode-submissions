class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dupes = set(nums)
        return len(nums) > len(no_dupes)
                
        