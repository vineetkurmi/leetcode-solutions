# Que. :- 53. Maximum Subarray
# Description :- Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentsum = nums[0]
        maxsum = nums[0]

        for i in range(1,len(nums)):
            currentsum = max(nums[i] , currentsum + nums[i])
            maxsum = max(maxsum , currentsum)

        return maxsum
