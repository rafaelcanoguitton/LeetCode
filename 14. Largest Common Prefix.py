from itertools import takewhile

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_chars = map(lambda x: x[0], takewhile(lambda x: all(x[0] == c for c in x), zip(*strs)))
        return ''.join(prefix_chars)