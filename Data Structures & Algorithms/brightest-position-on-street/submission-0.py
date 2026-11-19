class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        diff = defaultdict(int)
        
        for pos, rng in lights:
            start, end = pos - rng, pos + rng
            diff[start] += 1
            diff[end + 1] = -1

        max_bright = curr_bright = resp = 0

        for bright_pos in sorted(diff):
            curr_bright += diff[bright_pos]
            if curr_bright > max_bright:
                max_bright = curr_bright
                resp = bright_pos
        
        return resp