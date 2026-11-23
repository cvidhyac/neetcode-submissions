class Solution:
    from collections import defaultdict
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = defaultdict(int)
        for num in nums:
            if num in counter:
                return True
            else:
                counter[num] = 1
        return False