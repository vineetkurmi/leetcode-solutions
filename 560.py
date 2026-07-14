# Que. :- 560. Subarray Sum Equals K

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        currentsum = 0
        count = 0

        for i in nums:
            currentsum += i

            if currentsum - k in prefix:
                count += prefix[currentsum - k]
            
            prefix[currentsum] = prefix.get(currentsum, 0) + 1
        
        return count
