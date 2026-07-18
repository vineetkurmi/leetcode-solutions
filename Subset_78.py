# Que :- 78. Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Stores final answer
        res =[]

        # Current subset
        subset = []

        def backtrack(i):
            # Base case -> if all elements are processed
            if i == len(nums):

                # saving the copy of current subset
                res.append(subset[:])
                return

            # Choice 1 -> Take current element
            subset.append(nums[i])

            # Go to next element
            backtrack(i + 1)

            # Remove the current element
            subset.pop()

            # Choice 2 -> Don't take current element
            backtrack(i + 1)

        # Start Recursion index from 0
        backtrack(0)

        return res
