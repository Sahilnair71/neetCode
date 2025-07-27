# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

# time complexity:O(n)
# space complexity:O(n)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_set= {}
        l=0
        res=0
        for i in range(len(s)):
            if s[i] in temp_set:
                l= max(temp_set[s[i]]+1,l)
            temp_set[s[i]] =i
            res = max(res, i - l + 1)
            

           
        return res