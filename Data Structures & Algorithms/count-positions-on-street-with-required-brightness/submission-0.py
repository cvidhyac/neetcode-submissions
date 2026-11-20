class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        diff = defaultdict(int)
        for pos, rng in lights:
            start, end = pos - rng, pos + rng
            diff[max(0, start)] += 1
            diff[min(n - 1, end) + 1] -= 1

        current_brightness = answer = 0

        for i in range(n):
            current_brightness += diff[i]
            answer += current_brightness >= requirement[i]
        return answer