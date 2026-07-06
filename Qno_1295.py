# LeetCode 1295 – Find Numbers with Even Number of Digits

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            digit = 0

            while i != 0:
                digit += 1
                i //= 10
            
            if digit % 2 == 0:
                count += 1
        return count