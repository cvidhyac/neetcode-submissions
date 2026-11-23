class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list)
        for val in strs:
            as_ana = tuple(sorted(val))
            if as_ana in anagram_group.keys():
                ana_list = anagram_group[as_ana]
                ana_list.append(val)
                anagram_group[as_ana] = ana_list
            else:
                anagram_group[as_ana] = [val]
        return list(anagram_group.values())
