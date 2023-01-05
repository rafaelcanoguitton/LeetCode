class Solution:
    def isValid(self, s: str) -> bool:
        charmap ={
            '(':')',
            '{':'}',
            '[':']'
        }
        openingChars = {'(','{','['}
        storingChars = []
        for i in range(len(s)):
            if(s[i] in openingChars):
                storingChars.append(s[i])
            elif((not len(storingChars)) or charmap[storingChars.pop()]!=s[i]):
                return False
        return not len(storingChars)