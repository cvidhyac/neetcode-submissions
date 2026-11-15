class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        counter = 0
        for i in range(len(words) - 1):
            prefix_or_suffix = words[i]
            for j in range(i + 1, len(words)):
                the_word = words[j]
                if the_word.startswith(prefix_or_suffix) and the_word.endswith(prefix_or_suffix):
                    counter += 1
        return counter