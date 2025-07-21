# Question:
#Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

#You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Time complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dummy_hash ={}
        for index, item in enumerate(nums):
            find_element = target - item
            if find_element in dummy_hash:
                return [dummy_hash[find_element], index]
            else:
                dummy_hash[item]= index