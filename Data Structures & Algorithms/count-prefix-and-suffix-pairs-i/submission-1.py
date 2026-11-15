class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        counter = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                the_word = words[j]
                if the_word.startswith(words[i]) and the_word.endswith(words[i]):
                    counter += 1
        return counter