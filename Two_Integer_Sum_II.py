# Given an array of integers numbers that is sorted in non-decreasing order.

# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

# There will always be exactly one valid solution.


# Time complexity: O(n)
# Space Complexity: O(n)



class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)
        while( j>i):
            print(numbers[i])
            if (numbers[i] + numbers[j-1]) == target:
                return [i+1, j]
            elif (numbers[i] + numbers[j-1]) > target:
                 j-=1
            else:
                  i+=1 






               

        
        
        