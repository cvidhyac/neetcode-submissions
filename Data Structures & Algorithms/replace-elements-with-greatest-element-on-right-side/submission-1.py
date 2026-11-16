class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        a_copy = arr[::]
        for i in range(len(a_copy) - 1):
            right_max = -1
            for j in range(i+1, len(a_copy)):
                if a_copy[j] > right_max:
                    right_max = a_copy[j]
            a_copy[i] = right_max
        a_copy[-1] = -1
        return a_copy
                   