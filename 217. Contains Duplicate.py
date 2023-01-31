class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numberset = set()
        for num in nums:
            if num in numberset:
                return True
            else:
                numberset.add(num)
        return False