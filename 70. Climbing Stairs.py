class Solution:
    def climbStairs(self, n: int) -> int:
        #this is clearly fibonnacci sequence
        #and can be solved with dynamic programming
        climbed=[1,2,3]
        while (len(climbed)<n):# does this loop go forever?
            climbed.append(climbed[-1] + climbed[len(climbed)-2])
        return climbed[n-1]