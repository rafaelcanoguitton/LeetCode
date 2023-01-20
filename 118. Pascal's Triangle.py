class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        returnList = [[1],]
        while(len(returnList)!=numRows):
            toInsert = [1]
            for i in range(1,len(returnList[-1])):
                a = returnList[-1][i-1]
                b = returnList[-1][i]
                toInsert.append(a+b)
            toInsert.append(1)
            returnList.append(toInsert)
        return returnList