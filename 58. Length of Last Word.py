class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        copyOfString = s.strip()
        for i in range(len(copyOfString)-1,-1,-1):
            if copyOfString[i]==' ':
                break
            count+=1
        return count