class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        removedNums=set(nums)
        numsFixed = sorted(list(removedNums))
        for idx,num in enumerate(numsFixed):
            nums.insert(idx,num)
        return len(removedNums)