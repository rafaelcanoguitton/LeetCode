import math
class Solution:
    def mySqrt(self, x: int) -> int:
        #using newton's method
        if(x==0): return 0
        n = x
        l = 0.05
        count = 0
        while(True):
            count+=1
            root = 0.5*(x+(n/x))
            if(abs(root-x)<l):
                break
            x=root
        return math.floor(root)