class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        inc = deque([nums[0]])
        dec = deque([nums[0]])
        l = 0

        for r in range(1, len(nums)):
            while inc and inc[-1] > nums[r]:
                inc.pop()
            while dec and dec[-1] < nums[r]:
                dec.pop()

            inc.append(nums[r])
            dec.append(nums[r])

            if dec[0] - inc[0] > limit:
                if dec[0] == nums[l]:
                    dec.popleft()
                if inc[0] == nums[l]:
                    inc.popleft()
                l += 1
        return len(nums) - l