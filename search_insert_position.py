# You are given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Complexity: O(log(n))

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while(left<=right):
            print(left,"left")
            print(right,"right")
            med = int((left + right)/2)
            print(med)
            if nums[med] == target:
                return med
            elif nums[med] < target:
                left = med+1
            else:
                right = med -1
        return left
