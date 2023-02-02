class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alpha_map = {letter: index for index, letter in enumerate(order)}
        for i in range(len(words)-1):
            lower_len = min(len(words[i]), len(words[i+1]))
            contain = True
            for j in range(lower_len):
                if alpha_map[words[i][j]] > alpha_map[words[i+1][j]]:
                    return False
                elif alpha_map[words[i][j]] < alpha_map[words[i+1][j]]:
                    contain = False
                    break
            if contain and len(words[i])>len(words[i+1]):
                return False
        return True