class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        to_minutes = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)

        answer = 1440 + to_minutes[0] - to_minutes[-1] # 1440 + 0 - 1 = 1
        for i in range(1, len(to_minutes)):
            answer = min(answer, to_minutes[i] - to_minutes[i - 1])
        return answer
