from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_group = defaultdict(list)
        for val in strs:
            fingerprint = "".join(sorted(val))
            anagrams_group[fingerprint].append(val)
        return list(anagrams_group.values())

        