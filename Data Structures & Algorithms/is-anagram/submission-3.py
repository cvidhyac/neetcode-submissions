class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_str_s, sorted_str_t = sorted(s), sorted(t)
        return sorted_str_s == sorted_str_t