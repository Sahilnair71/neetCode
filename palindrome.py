# Question:
#Given a string s, return true if it is a palindrome, otherwise return false.
#A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
# Time complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
       changed_list=[]
       for i in s:
        if i.isalnum():
            changed_list.append(i.lower())
       i=0
       j=len(changed_list)-1
       while(i<=j):
        if changed_list[i] != changed_list[j]:
            return False
        else:
            i+=1
            j-=1
       return True

            
       
    
        
    
        
        
        