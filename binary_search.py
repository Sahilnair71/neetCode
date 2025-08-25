# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

# Your solution must run in 

# O(logn) time.



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length= len(nums)
        right =length-1
        left = 0
        if nums[left] == target:
            return left
        elif nums[right]== target:
            return right
        else:
            while (left<=right):
                mid = int((left + right)/2)
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    right = mid-1
                else:
                    left = mid+1
            return -1
        