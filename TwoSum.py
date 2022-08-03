def twoSum(nums, target):
    numberHash = {}
    for i in range(len(nums)):
        complement = target-nums[i]
        if complement in numberHash:
            return [numberHash[complement],i]
        numberHash[nums[i]] = i



numbers = [int(x) for x in input().split(" ")]
target = int(input())
print(twoSum(numbers, target))
