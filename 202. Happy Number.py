from functools import reduce
class Solution:
    def isHappy(self, n: int) -> bool:
        setOfNumbers = set()
        actualNumber = n
        while(actualNumber != 1 and actualNumber not in setOfNumbers):
            setOfNumbers.add(actualNumber)
            actualNumber = reduce(lambda x,y: x+y,[int(x)**2 for x in str(actualNumber)])
        return actualNumber == 1
