class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic={}
        for i in range(len(nums)):
            if nums[i] not in dic.keys():
                dic[target-nums[i]]=i
            else:
                return [dic[nums[i]],i]