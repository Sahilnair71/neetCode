# ou are given an m x n 2-D integer array matrix and an integer target.

# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.

# Can you write a solution that runs in O(log(m * n)) time?

# time complexity :O(m + log n)




class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            length = len(i)-1
            if i[0]<=target<=i[length]:
                res=self.binary_search(i,target)
                return res
        return False
    

    def binary_search(self,nums,target):
        length= len(nums)
        right =length-1
        left = 0
        if nums[left] == target:
            return True
        elif nums[right]== target:
            return True
        else:
            while (left<=right):
                mid = int((left + right)/2)
                if nums[mid]==target:
                    return True
                elif nums[mid]>target:
                    right = mid-1
                else:
                    left = mid+1
            return False
        