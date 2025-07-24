# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

# Solution Conplexit:
# Time complexity: O(n2)
# Space Complexity: O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        length=len(nums)-2
        nums.sort()
        for i in range(0, length):
            if i>0 and nums[i] == nums[i-1]:
                continue

            target= nums[i]
            target = -target
            j=i+1
            k= len(nums)-1
            print(target,"target")
            
            while(j<k):
               
                sum_val= nums[j] + nums[k]
                print(sum_val,"sum_val")
                if sum_val == target:
    
                    res.append([-target,nums[j],nums[k]])
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j +=1
                elif sum_val > target:
                    k-=1
                else:
                    j+=1
        return res


                    

                    

        