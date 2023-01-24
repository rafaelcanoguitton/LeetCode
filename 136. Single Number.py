class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numberset = set()
        for num in nums:
            if num in numberset:
                numberset.remove(num)
            else:
                numberset.add(num)
        for num in numberset:
            return num