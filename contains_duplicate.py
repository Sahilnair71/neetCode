# Question:
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Solution Conplexit:
# Time complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_code = set(nums)
        if(len(nums)>len(hash_code)):
            return True
        else:
            return False

