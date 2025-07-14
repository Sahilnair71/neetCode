# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# Solution Conplexit:
# Time complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if self.hashFunction(s) == self.hashFunction(t):
            return True
        else:
            return False

    


    def hashFunction(self,str):
        dictionary = {}
        for char in str:
            if char in dictionary:
                dictionary[char]+=1
            else:
                dictionary[char]=1

        return dictionary
        