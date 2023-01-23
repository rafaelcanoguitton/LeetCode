class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c.lower() for c in s if c.isalnum()])
        beginIndex = 0
        endIndex = len(s)-1
        while(beginIndex<endIndex):
            if s[beginIndex] != s[endIndex]:
                return False
            beginIndex+=1
            endIndex-=1
        return True